import chess
import chess.svg
import chess.polyglot
import chess.pgn
import traceback
import webbrowser
import time
import random
from flask import Flask, Response, request


# Choosing engine move by randomly selecting a move from the list of legal moves
def engineMove():
    current_moves = []
    for i in board.legal_moves:
      current_moves.append(i)
    move = random.choice(current_moves)
    board.push(move)

# webapp setup

app = Flask(__name__)

@app.route("/")
def main():
    global count, board
    if count == 1:
        None
        count += 1
    ret = '<html><head>'
    ret += '<style>input {font-size: 20px; } button { font-size: 20px; }</style>'
    ret += '</head><body>'
    ret += '<h1>RandomMove Chess engine</h1>'
    ret += '<p>Input moves by typing into box next to make human move and clicking to submit</p>'
    ret += '<p>To receive engine moves click make engine move</p>'
    ret += '<p>This engine works by making a random legal move.</p>'
    ret += '<img width=510 height=510 src="/board.svg?%f"></img></br>' % time.time()
    ret += '<form action="/game/" method="post"><button name="New Game" type="submit">New Game</button></form>'
    ret += '<form action="/undo/" method="post"><button name="Undo" type="submit">Undo Last Move</button></form>'
    ret += '<form action="/move/"><input type="submit" value="Make Human Move:"><input name="move" type="text"></input></form>'
    ret += '<form action="/dev/" method="post"><button name="Comp Move" type="submit">Make engine move</button></form>'

    if board.is_stalemate():
        print("Its a draw by stalemate")
        ret += '<h3>Draw by stalemate</h3>'
    elif board.is_checkmate():
        print("Checkmate")
        ret += '<h3>Checkmate</h3>'
    elif board.is_insufficient_material():
        print("Its a draw by insufficient material")
        ret += '<h3>Draw by insufficient material</h3>'
    elif board.is_check():
        print("Check")
        ret += '<h3>check</h3>'
    return ret

# Display Board
@app.route("/board.svg/")
def board():
    return Response(chess.svg.board(board=board, size=700), mimetype='image/svg+xml')

# Human Move
@app.route("/move/")
def move():
    try:
        move = request.args.get('move', default="")
        board.push_san(move)
    except Exception:
        traceback.print_exc()
    return main()

# Recieve Human Move
@app.route("/recv/", methods=['POST'])
def recv():
    try:
        None
    except Exception:
        None
    return main()

@app.route("/dev/", methods=['POST'])
def dev():
    try:
        engineMove()
    except Exception:
        traceback.print_exc()
    return main()

# New Game
@app.route("/game/", methods=['POST'])
def game():
    board.reset()
    return main()

# Undo
@app.route("/undo/", methods=['POST'])
def undo():
    try:
        board.pop()
    except Exception:
        traceback.print_exc()
    return main()

if __name__ == '__main__':
    count = 1
    board = chess.Board()
    webbrowser.open("http://127.0.0.1:5000/")
    app.run()

