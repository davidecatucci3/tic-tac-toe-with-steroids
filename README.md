# tic-tac-toe-with-steroids
Tic Tac Toe engine that used minmax algorithm that plays always optimally, impossible to defeat (try!)

> A command-line Tic-Tac-Toe game in Python — with a Minimax AI opponent and full dialogue in Sicilian dialect.

---

## Overview

A fully playable Tic-Tac-Toe (Tris) game that runs in the terminal. The player goes up against a computer opponent that uses the **Minimax algorithm** to play optimally — it will never lose. All in-game messages are written in Sicilian dialect, giving the game a very particular personality.

---

## How It Works

1. **Sign selection** — The player chooses `X` or `O` (or `no` to quit before starting).
2. **Player turn** — The player inputs a board position as `row col` (e.g. `1 1` for the center).
3. **AI turn** — The computer uses Minimax to pick the optimal move.
4. **Win check** — After every turn, rows, columns, and diagonals are checked for a winner.
5. **Rematch** — After a win or tie, the player is asked `si` / `no` to play again.

---

## Project Structure

```
.
├── main.py         # Game loop, board logic, player/AI turns, win detection
└── minmax.py       # MinMax class implementing the Minimax algorithm
```

---

## Requirements

- Python 3.8+
- No external dependencies — standard library only

---

## Usage

```bash
python main.py
```

### Example Session

```
Jucamo, che vulissi, a X o la O? x

Jucamo a X!

. . .
. . .
. . .

Combacri addu la nziccamo sta x?  1 1

. . .
. x .
. . .

[AI moves...]
```

### Input Format

| Prompt | Expected input |
|---|---|
| Sign selection | `x`, `o`, or `no` (to quit) |
| Position | `row col` — two space-separated integers from `0` to `2` |
| Rematch | `si` or `no` |

### Board Layout

Positions are zero-indexed — `row col` from `0 0` (top-left) to `2 2` (bottom-right):

```
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

---

## AI

The computer uses the **Minimax algorithm** (implemented in `minmax.py`) to evaluate every possible game state and always pick the move with the best outcome. It plays perfectly — the best result a human can achieve against it is a draw.

Random move mode is also available in `p1_turn()` (pass `ai=False`) for a much easier opponent.

---

## Dialogue

All prompts and responses are written in **Sicilian dialect**. A few highlights:

| Situation | Message |
|---|---|
| Player picks X | *"E si nu cazz'i butirro pure tu eh?!"* |
| Player picks O | *"E si nu cazz'i buttigghiuno"* |
| Invalid position | *"Ma cu t'ambarato, i vu minde dui numeri justi ingegné?"* |
| Cell already taken | *"Allora si cugghiuno, vida i cangia posto..."* |
| Player wins | *"Hai vinto, Tantu piaciro allu cazzu dotto, Ama rifa?"* |
| Player loses | *"Hai perso, T'avissa frica n'gapo stu cazz'i juco"* |
| Tie | *"Abbiamo pareggiato, ama rijuca'?"* |

---

## Known Issues

There is a copy-paste bug in `is_win()` — the second anti-diagonal check compares against `self.p2` instead of `self.p1`:

```python
# Bug — both branches check p2, so p1 can never win via anti-diagonal:
elif [self.board[0][2], self.board[1][1], self.board[2][0]].count(self.p2) == 3:
    self.winner = self.p1   # ← assigns p1 but condition checks p2

# Fix:
elif [self.board[0][2], self.board[1][1], self.board[2][0]].count(self.p1) == 3:
    self.winner = self.p1
```

Also, `p2_turn()` and `p1_turn()` use recursion for input retries — deep invalid input chains could hit Python's recursion limit. An iterative loop would be safer.

---

## License

MIT License. See `LICENSE` for details.
