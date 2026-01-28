# 🐍 Enhanced Snake Game

A modern, feature-rich Snake game built with Python and Turtle graphics. This enhanced version includes improved gameplay mechanics, better visuals, persistent high scores, and multiple game states.

## ✨ Features

- **Modern UI**: Clean, dark theme with vibrant colors
- **Game States**: Start screen, pause functionality, and game over screen
- **Persistent High Score**: Automatically saves and loads your best score
- **Smooth Gameplay**: Optimized movement and collision detection
- **Progressive Difficulty**: Game speed increases as you score more points
- **Smart Food Placement**: Food never spawns on the snake's body
- **Better Controls**: Intuitive keyboard controls with pause functionality

## 🎮 Game Controls

| Key | Action |
|-----|--------|
| **Arrow Keys** | Move the snake (Up, Down, Left, Right) |
| **SPACE** | Start game / Play again after game over |
| **P** | Pause/Resume game |
| **Q** | Quit game (only available on game over screen) |

## 🚀 How to Run the Game

### Prerequisites

1. **Python Installation**: Make sure you have Python 3.6 or higher installed on your system.
   - Download from: https://www.python.org/downloads/
   - During installation, make sure to check "Add Python to PATH"

2. **Verify Python Installation**:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

### Step-by-Step Instructions

#### Method 1: Using Command Line

1. **Open Command Prompt/Terminal**:
   - **Windows**: Press `Win + R`, type `cmd`, press Enter
   - **Mac**: Press `Cmd + Space`, type `Terminal`, press Enter
   - **Linux**: Press `Ctrl + Alt + T`

2. **Navigate to the Game Directory**:

   cd "d:\MyProjects\SnakeGame"
  

3. **Run the Game**:
  
   python SnakeGame.py
 
   
   If the above doesn't work, try:
   
   python3 SnakeGame.py
   

#### Method 2: Using File Explorer (Windows)

1. **Navigate to the Game Folder**:
   - Open File Explorer
   - Go to `d:\MyProjects\SnakeGame`

2. **Run the Game**:
   - Right-click on `SnakeGame.py`
   - Select "Open with" → "Python"
   - Or double-click if Python is set as default for `.py` files

#### Method 3: Using Python IDE

1. **Open your Python IDE** (IDLE, PyCharm, VS Code, etc.)
2. **Open the file**: `SnakeGame.py`
3. **Run the script**: Press F5 or click the Run button

## 🎯 How to Play

1. **Start the Game**: Press SPACE when you see the start screen
2. **Control the Snake**: Use arrow keys to move the snake around
3. **Eat Food**: Guide the snake to the red circular food
4. **Avoid Collisions**: Don't hit the walls or your own body
5. **Score Points**: Each food eaten gives you 10 points
6. **Beat Your High Score**: Try to beat your previous best score!

## 🏆 Scoring System

- **Points per Food**: 10 points
- **Speed Increase**: Game gets faster as you score more
- **High Score**: Automatically saved and persists between game sessions
- **High Score File**: Stored in `high_score.txt` in the game directory

## 🔧 Game Mechanics

### Snake Movement
- Snake moves continuously in the current direction
- Cannot reverse directly into itself
- Movement is grid-based (20-pixel increments)

### Collision Detection
- **Wall Collision**: Game ends when snake hits any wall
- **Self Collision**: Game ends when snake hits its own body
- **Food Collision**: Snake grows and score increases

### Difficulty Progression
- Initial speed: 0.15 seconds per move
- Speed increases by 0.001 seconds with each food eaten
- Minimum speed: 0.08 seconds per move

## 📁 File Structure

```
SnakeGame/
├── SnakeGame.py      # Main game file
├── README.md         # This file
└── high_score.txt    # High score storage (created automatically)
```

## 🐛 Troubleshooting

### Common Issues and Solutions

1. **"Python is not recognized as an internal or external command"**
   - Solution: Add Python to your system PATH or reinstall Python with "Add to PATH" checked

2. **Game window doesn't appear**
   - Solution: Make sure you have tkinter installed (usually comes with Python)
   - Try: `pip install tk`

3. **Game runs but controls don't work**
   - Solution: Click on the game window to ensure it has focus

4. **High score not saving**
   - Solution: Make sure the game directory has write permissions

5. **Game is too fast/slow**
   - Solution: You can modify the `INITIAL_DELAY` constant in the code (line 11)

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.6 or higher
- **Memory**: Minimal (< 50 MB)
- **Graphics**: Basic display capability

## 🎨 Customization

You can easily customize the game by modifying these constants at the top of `SnakeGame.py`:

```python
WIDTH = 600           # Game window width
HEIGHT = 600          # Game window height
MOVE_DISTANCE = 20    # Snake movement distance
INITIAL_DELAY = 0.15  # Starting game speed
SCORE_INCREMENT = 10  # Points per food
```

### Color Customization

Change these colors in the respective methods:
- **Background**: `#1a1a2e` (dark blue)
- **Snake Head**: `#00ff41` (bright green)
- **Snake Body**: `#4ecdc4` (teal)
- **Food**: `#ff6b6b` (red)

## 🤝 Contributing

Feel free to fork this project and submit improvements! Some ideas for enhancements:
- Add sound effects
- Implement different game modes
- Add power-ups
- Create different snake skins
- Add multiplayer support

## 📝 License

This project is open source and available under the MIT License.

---

**Enjoy playing the Enhanced Snake Game! 🐍🎮**