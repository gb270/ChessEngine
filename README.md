# ChessEngine
The aim of this project is to create a chess engine using python. 

A chess engine is defined as 'a computer program that analyzes chess or chess variant positions, and generates a move or list of moves that it regards as strongest'.

This project was inspired by the Chess-World project. The code for setting up the webapp using flask has been reused from that project. You can access that project [here](https://github.com/AnshGaikwad/Chess-World).

### RandomMove

The first engine that was produced is one that simply plays a random legal move. Hence, it is relatively easy to beat. The engine takes a position and using the [chess](https://python-chess.readthedocs.io/en/latest/) python module chooses a random legal move to play.

### What's next?

The next steps of the project are to implement an algorithm that can evaluate a position one move ahead. Going forwards the project aims to replicate traditional chess engines by utilising Alpha-beta pruning on a minimax algorithm. 

