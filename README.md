# Snake Game AI with Deep Q-Learning and Obstacle Avoidance

This project implements a **Snake Game** in Python with two modes:
1. **Manual Mode (`new_game.py`)** – Play Snake manually using the arrow keys, with randomly placed obstacles.
2. **AI Mode (`agent.py` + `game.py`)** – Train a reinforcement learning agent (Deep Q-Learning with PyTorch) to play Snake autonomously.

The project includes visualization of training progress and uses function approximation (a neural network) to estimate Q-values.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Game Modes](#game-modes)
- [Reinforcement Learning Setup](#reinforcement-learning-setup)
- [Files in the Repository](#files-in-the-repository)
- [Setup](#setup)
- [Usage](#usage)
- [Results](#results)

---

## Project Overview

The Snake Game has been extended with:
- **Obstacles:** Randomly generated blocks the snake must avoid.
- **Food Placement:** Randomized while ensuring it does not overlap with the snake or obstacles.
- **AI Agent:** Uses **Deep Q-Learning (DQN)** to learn optimal strategies.

The agent is trained with **experience replay** and an **epsilon-greedy policy** to balance exploration and exploitation.

---

## Game Modes

### 1. Manual Play (`new_game.py`)
- Control the snake using **arrow keys**.
- The snake grows when it eats food.
- The game ends when the snake collides with the wall or obstacles.

### 2. AI Play (`agent.py` + `game.py`)
- The agent perceives the environment as a state vector of 11 features:
  - Immediate dangers (straight, left, right).
  - Current movement direction.
  - Relative position of food.
- The agent outputs one of four moves:
  - `[1, 0, 0, 0]` → Straight  
  - `[0, 1, 0, 0]` → Turn Right  
  - `[0, 0, 1, 0]` → Turn Left  
  - `[0, 0, 0, 1]` → Reverse (safety move)  

Rewards:
- `+10` for eating food  
- `-10` for collisions or exceeding a step limit  
- `0` otherwise  

---

## Reinforcement Learning Setup

- **Algorithm:** Deep Q-Learning (DQN)  
- **Model:** A two-layer fully connected network (`Linear_Qnet`) with ReLU activation.  
- **Trainer:** Custom Q-learning update loop (`QTrainer`).  
- **Memory:** Replay buffer with a maximum size of 100,000 experiences.  
- **Batch Training:** Random mini-batches sampled for stability.  
- **Exploration Strategy:** Epsilon-greedy with decreasing randomness over episodes.  

---

## Files in the Repository

- **`new_game.py`** – Manual snake game with obstacles.  
- **`game.py`** – Snake game environment for the AI agent.  
- **`agent.py`** – Reinforcement learning agent (DQN) and training loop.  
- **`model.py`** – Neural network model (`Linear_Qnet`) and Q-learning trainer.  
- **`helper.py`** – Visualization utility for training scores (live matplotlib plots).  
- **`arial.ttf`** – Font file for rendering text in Pygame.  

---

## Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Devesh176/Snake_Game_RL.git
   cd Snake_Game_RL/pygame_env_rl
   ```

2. **Install the Dependencies**
   ```bash
   pip install pygame torch matplotlib
   ```
3. **Ensure the font file is present** (arial.ttf)


## Usage

1. **To play the game manually**
   ```bash
   python new_game.py
   ```
2. **Train the AI Agent**
   ```bash
   python agent.py
   ```
## Results
During training:
- A live plot of scores and mean scores is displayed using matplotlib.
- The agent gradually improves performance over multiple games.
   
   
   
