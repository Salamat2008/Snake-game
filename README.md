# 🐍 Snake Game

A simple Snake game implementation using Python and Pygame.

## Features

- Classic snake gameplay
- Grid-based movement
- Food spawning system
- Score tracking
- Game over detection
- Restart functionality

## Requirements

- Python 3.6+
- Pygame

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Salamat2008/Snake-game.git
cd Snake-game
```

2. Install pygame:
```bash
pip install pygame
```

## How to Play

Run the game:
```bash
python main.py
```

### Controls

- **Arrow Keys** - Move the snake (Up, Down, Left, Right)
- **SPACE** - Restart the game after game over

### Gameplay

- The snake starts in the middle of the screen
- Eat the red food squares to grow and increase your score
- Don't hit the walls or yourself!
- Each food eaten gives 10 points
- Press SPACE to restart after a game over

## Game Speed

The game runs at 10 FPS for comfortable gameplay. You can adjust this value in `main.py`:
```python
self.clock.tick(10)  # Change 10 to a higher value for faster gameplay
```

## Code Structure

- `SnakeGame` - Main game class handling all game logic
- `Direction` - Enum for snake movement directions
- `handle_input()` - Processes keyboard input
- `update()` - Updates game state
- `draw()` - Renders game elements

## License

Feel free to use and modify this code!
