# 🐍 Local Multiplayer Snake 

A competitive, fast-paced multiplayer twist on the classic Snake game. This game is specifically designed for **two players to play simultaneously on the exact same keyboard**, making it perfect for quick local versus matches!

<img width="407" height="443" alt="Screenshot from 2026-07-09 16-23-07" src="https://github.com/user-attachments/assets/cb5224f9-540b-40f5-ba7d-13b97ece9b06" />


## 🎮 How to Play on the Same Device
No network setup, servers, or second controllers required! Both players simply sit at the same computer and share the keyboard. 
* **Player 1** commands the left side of the keyboard (WASD).
* **Player 2** commands the right side of the keyboard (↑←↓→).

### 🕹️ Controls

Player 1 (Blue Snake):         ^
                            <  ⌄  >
                            
Player 2 (Green Snake):        W
                            A  S  D


## ⚔️ Game Rules & Mechanics
* **Objective:** Outgrow and outlast your opponent.
* **Wrap-Around Map:** There are no walls! Moving off the edge of the screen teleports you to the opposite side. Use this to ambush your opponent!
* **Collisions:** * If you crash into your opponent's body, **they win**.
    * If you crash into your own body, **your opponent wins**.
* **Food Elements:**
    * 🍎 **Pink Food:** Standard food. Grants +1 Point and +1 Length.
    * 🍔 **Gold Bonus Food:** Spawns randomly. Grants +3 Points and +3 Length. Grab it before your opponent does!

## 🚀 Installation & Setup
1. Ensure you have **Python 3.x** installed on your system.
2. Install the required graphics library, `pygame`:
```bash
pip install pygame
```
3. Run the game:
for Windows:
```bash
python snakeLMP.py
```
for Linux/Mac
```bash
python3 snakeLMP.py
```

