# Rubik's Cube Visualizer (2x2 & 3x3)

This Python tool visualizes the transformation of a scrambled Rubik's Cube (2×2 or 3×3) into a solved state. It uses `matplotlib` to display each step as a 2D net.

## Features

- Supports both 2×2 and 3×3 cubes
- Visual step-by-step solving (morphing simulation)
- Saves each step as an image
- Easy-to-use CLI input format

## How It Works

This is not a full Rubik’s Cube solver — instead, it visually "morphs" the scrambled state into a solved state to illustrate progress toward the solution.

## Input Format

Enter a single string with:
- **54 characters** for 3x3
- **24 characters** for 2x2  
Use characters: `W`, `Y`, `R`, `O`, `B`, `G` (white, yellow, red, orange, blue, green)

**Face order:** `U`, `R`, `F`, `D`, `L`, `B`  
Example for 2x2:
