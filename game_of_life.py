import time
import os
import random

# Constants for the grid
WIDTH = 40
HEIGHT = 20
LIVE = "\u2588"  # Unicode full block for a "live" cell
DEAD = " "

def create_grid():
    """Initializes a grid with random life."""
    return [[random.choice([LIVE, DEAD, DEAD, DEAD]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_grid(grid):
    """Simple graphics demonstration using terminal output."""
    os.system('clear' if os.name == 'pos' else 'cls')
    print("=== Conway's Game of Life (Iteration Demo) ===")
    for row in grid:
        print("".join(row))
    print("\nPress Ctrl+C to stop.")

def get_next_state(grid):
    """
    Calculates the next state of the board.
    
    ITERATION SECTION:
    This function uses nested loops (Iteration) to visit every cell 
    in the 2D grid and apply the rules of life based on neighbors.
    """
    new_grid = [[DEAD for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # OUTER ITERATION: Loop through each row
    for y in range(HEIGHT):
        # INNER ITERATION: Loop through each column
        for x in range(WIDTH):
            # 1. Count live neighbors
            neighbors = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0: continue
                    ny, nx = (y + dy) % HEIGHT, (x + dx) % WIDTH
                    if grid[ny][nx] == LIVE:
                        neighbors += 1
            
            # 2. Apply Conway's Rules
            current = grid[y][x]
            if current == LIVE and (neighbors == 2 or neighbors == 3):
                new_grid[y][x] = LIVE
            elif current == DEAD and neighbors == 3:
                new_grid[y][x] = LIVE
            else:
                new_grid[y][x] = DEAD
                
    return new_grid

def main():
    grid = create_grid()
    try:
        # INFINITE ITERATION: The simulation loop
        while True:
            print_grid(grid)
            grid = get_next_state(grid)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
