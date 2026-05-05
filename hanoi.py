import time
import os

def hanoi(n, source, target, auxiliary):
    """
    Tower of Hanoi - A classic demonstration of RECURSION.
    
    RECURSION SECTION:
    The function calls itself with a smaller problem size (n-1).
    This breaks down the complex task of moving 'n' disks into 
    moving 'n-1' disks twice, with a single base move in between.
    """
    if n > 0:
        # Recursive Step 1: Move n-1 disks to the auxiliary peg
        hanoi(n - 1, source, auxiliary, target)
        
        # Base Action: Move the largest disk to the target peg
        print(f"  Disk {n}: {source} \u27f6 {target}")
        
        # Recursive Step 2: Move the n-1 disks from auxiliary to the target peg
        hanoi(n - 1, auxiliary, target, source)

def main():
    os.system('clear' if os.name == 'pos' else 'cls')
    print("=== Tower of Hanoi (Recursion Demo) ===")
    n = 3  # Number of disks
    print(f"Solving for {n} disks:\n")
    
    # Starting the recursive process
    hanoi(n, 'Peg A', 'Peg C', 'Peg B')
    
    print("\nRecursion Complete.")

if __name__ == "__main__":
    main()
