#!/bin/bash

# ==============================================================================
# RISC-V High Precision Code Base - Demo Suite
# ==============================================================================
# This script demonstrates Recursion and Iteration using simple terminal graphics.
# ==============================================================================

# --- RECURSION DEMONSTRATION (Tower of Hanoi) ---
# Function: move_disks
# Description: Moves n disks from source to destination using an auxiliary peg.
move_disks() {
    local n=$1
    local source=$2
    local destination=$3
    local auxiliary=$4

    # RECURSION SECTION:
    # If n is greater than 0, we split the problem into smaller sub-problems.
    if [ $n -gt 0 ]; then
        # 1. Recursive call: Move n-1 disks to auxiliary
        move_disks $((n - 1)) "$source" "$auxiliary" "$destination"
        
        # 2. Base move: Move the nth disk
        echo "  Move disk $n from $source to $destination"
        
        # 3. Recursive call: Move n-1 disks from auxiliary to destination
        move_disks $((n - 1)) "$auxiliary" "$destination" "$source"
    fi
}

# --- ITERATION DEMONSTRATION (Simple Counter / Pulse) ---
# This is a simpler iteration example if the Python scripts aren't preferred.
run_pulse() {
    echo "Starting Iteration Pulse..."
    # ITERATION SECTION:
    # A standard 'for' loop that repeats a specific number of times.
    for i in {1..10}; do
        echo -ne "  Pulse $i: ["
        for ((j=0; j<i; j++)); do echo -ne "#"; done
        for ((j=i; j<10; j++)); do echo -ne "."; done
        echo -ne "]\r"
        sleep 0.2
    done
    echo -e "\nIteration Pulse Complete."
}

# --- MAIN MENU ---
clear
echo "==============================================="
echo "   RISC-V High Precision Demo Suite"
echo "==============================================="
echo "1) Tower of Hanoi (Recursion - Bash)"
echo "2) Game of Life (Iteration - Python)"
echo "3) Pulse Demo (Iteration - Bash)"
echo "4) Exit"
echo "==============================================="
read -p "Select a demo: " choice

case $choice in
    1)
        echo -e "\n--- Tower of Hanoi (Recursion) ---"
        move_disks 3 "Peg-A" "Peg-C" "Peg-B"
        ;;
    2)
        if command -v python3 &>/dev/null; then
            python3 "$(dirname "$0")/game_of_life.py"
        else
            echo "Python3 not found. Please run game_of_life.py manually."
        fi
        ;;
    3)
        run_pulse
        ;;
    4)
        exit 0
        ;;
    *)
        echo "Invalid selection."
        ;;
esac
