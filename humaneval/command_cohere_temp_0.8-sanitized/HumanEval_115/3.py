import math
def max_fill(grid, capacity) :
    # Initialize counter to 0
    count = 0
    # Nested loop to iterate through every cell in the 2D array
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Increase count if the current cell has water
            if(grid[i][j] == 1):
                count += 1
            # Decrease count if the counter exceeds the capacity
            else:
                count = count - 1
                if count < 0:
                    count = 0
    return count