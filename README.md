# Terminal Adventure Game

A lightweight, text-based interactive adventure game built in Python. The game features non-linear room exploration, inventory mechanics, puzzle solving, multiple win conditions, and fail states.

This project was built with the assistance of GitHub Copilot as part of the Global Hack Week Hacktoberfest challenge.

---

## Features

- **Branching Decision Paths:** Multiple navigational routes and encounter options based on player decisions.
- **Inventory & Item Gating:** Collect items necessary to unlock doors, bypass obstacles, or access alternate narrative paths.
- **Multiple Endings:** Two distinct victory conditions alongside several failure states.
- **Replayability:** In-game prompt allows players to immediately restart after a win or loss.
- **Zero External Dependencies:** Built entirely with Python's standard library.

---

## Prerequisites

- **Python 3.8+** installed on your system.

To verify your installation, run:

```bash
python --version
```
*(On macOS/Linux systems, use `python3` instead of `python` if required).*

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Run the game:**
   ```bash
   python game.py
   ```

---

## How to Play

1. Follow the on-screen narrative descriptions.
2. Enter the corresponding numerical input (e.g., `1`, `2`, `3`) at each prompt to make your choice.
3. Manage your inventory by picking up tools and clues scattered throughout different rooms.
4. Choose carefully—certain paths lead to traps or dead ends.

---

## Project Structure

```text
.
├── game.py       # Main game loop, state management, and narrative logic
└── README.md     # Project documentation
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).