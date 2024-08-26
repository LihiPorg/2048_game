# 2048_game
2048 game I implemented in 2020 using python. The goal is to combine tiles with the same numbers using the arrows keys to reach the 2048 tile.

## Features

- **Basic Movement**: Move the tiles left, right, up, and down using the arrow keys.
- **Automatic Tile Addition**: A new tile with a value of 2 or 4 is added to the board after each move.
- **Winning and Losing Conditions**: The game ends if you create a 2048 tile (win) or if there are no available moves (lose).

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install the required dependencies:

    ```bash
    pip install pygame
    ```

4. Run the game:

    ```bash
    python main.py
    ```

## Controls

- **Left Arrow**: Move tiles to the left
- **Right Arrow**: Move tiles to the right
- **Up Arrow**: Move tiles upwards
- **Down Arrow**: Move tiles downwards

## Gameplay

- Combine tiles with the same number to create a new tile with their sum.
- The game is won when a tile with the number 2048 is created.
- The game ends if there are no more valid moves.

## License

This project is licensed under the MIT License. 


