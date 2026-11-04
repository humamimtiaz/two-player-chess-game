# Two-Player Chess Game

A desktop chess game built with Python and Pygame. Two players can play locally on the same computer using the mouse.

## Features
- Graphical 8×8 chessboard with separate white and black piece sprites
- Turn-based, two-player gameplay
- Piece selection and visual highlighting of available moves
- Movement logic for pawns, rooks, knights, bishops, queens, and kings
- Capturing opposing pieces and displaying captured pieces
- Visual warning when a king is under attack
- Restart option after a king is captured

## Tech Stack
- Python
- Pygame

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/two-player-chess-game.git
cd two-player-chess-game
```

### 2. (Recommended) Create and activate a virtual environment
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS / Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the game
```bash
python main.py
```

## How to Play
1. Run the game.
2. White and Black take turns.
3. Click a piece to select it; available destination squares are shown.
4. Click a highlighted square to move the selected piece.
5. Capture the opposing king to end the game.
6. Press **Enter** to restart after the game ends.
7. Close the game window to exit.

## Project Structure
```text
two-player-chess-game/
├── assets/
│   └── images/          # Chess piece sprites
├── main.py              # Game loop, board rendering, and move logic
├── requirements.txt
├── .gitignore
└── README.md
```

## Current Scope / Limitations
This is an educational two-player chess project, not a complete tournament-rules chess engine. The current implementation does not include castling, en passant, pawn promotion, or full check/checkmate and stalemate validation. The game ends when a king is captured.

## Notes
The original project environment and IDE-specific files are intentionally excluded. Install dependencies from `requirements.txt` instead of uploading a local virtual environment.
