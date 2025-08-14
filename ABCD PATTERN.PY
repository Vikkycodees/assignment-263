n = 5  # Number of rows (max letter = E)

for i in range(n, 0, -1):
    # Left side (A to ith letter)
    for j in range(i):
        print(chr(65 + j), end=" ")
    
    # Spaces in the middle
    print("  " * (n - i), end="")
    
    # Right side (reverse from ith letter to A)
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end=" ")
    
    print()
