 🐍 Jaswanth Snake Game

A simple and fun **Snake Game** built using **Python** and **Pygame**.

---

## 📌 Project Title:
**Jaswanth Snake Game using Python and Pygame**

---

## 📝 Introduction

This is a basic implementation of the classic **Snake Game** built using Python’s `pygame` module. The player controls a snake that moves around the screen, eats food to grow longer, and loses if it collides with itself. This project helps in understanding key concepts like **game loops**, **user input**, **collision detection**, and **graphics rendering**.

---

## 🎯 Objective

- Create an interactive snake game in Python.
- Practice using the `pygame` library.
- Learn game mechanics like:
  - Keyboard controls
  - Object movement
  - Collision detection
  - Object rendering

---

## 🔧 Tools & Technologies Used

| Tool            | Purpose                             |
|-----------------|-------------------------------------|
| Python 3.x      | Main programming language           |
| Pygame          | Game development library            |
| VS Code / IDLE  | Code editor / IDE                   |

---

## ✨ Features

- Real-time snake movement with arrow keys.
- Food appears randomly on the screen.
- Snake grows upon eating food.
- Screen wrapping when snake hits wall.
- Game ends when the snake hits itself.

---

## 📂 Folder Structure

snake_game/
│
├── snake_game.py # Main game file
├── README.md # Project documentation
└── requirements.txt # Pygame dependency (optional)

yaml
Copy
Edit

---

## 🧾 Code Overview

### 🎮 Game Initialization
```python
pygame.init()
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jaswanth Snake Game")
🐍 Snake & Food Setup
python
Copy
Edit
snake_x, snake_y = width // 2, height // 2
food_x = random.randrange(0, width, 10)
food_y = random.randrange(0, height, 10)
🎯 Controls and Movement
python
Copy
Edit
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        change_x, change_y = -10, 0
🍽️ Eating Food and Growing
python
Copy
Edit
if snake_x == food_x and snake_y == food_y:
    # Grow snake and reposition food
💥 Game Over Detection
python
Copy
Edit
if (snake_x, snake_y) in snake_body[1:]:
    print("GAME OVER")
    pygame.quit()
    quit()
💻 How to Run the Game
Install Python (if not installed)

Install Pygame:

bash
Copy
Edit
pip install pygame
Run the game:

bash
Copy
Edit
python snake_game.py
📸 Output Preview
Snake moves on screen using arrow keys.

Eats colored food and grows in length.

Game ends when it hits its own body.

🚀 Future Improvements
Add score tracking

Add start and game over screens

Add sound effects and music

Add obstacles for difficulty

📜 License
This project is for learning and personal use.

👨‍💻 Developed by
Budili Jaswanth Reddy
