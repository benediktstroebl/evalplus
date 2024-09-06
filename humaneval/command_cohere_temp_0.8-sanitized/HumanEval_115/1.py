import math
def max_fill(grid, capacity):
    bucket_movements = 0

    # Iterate through each row (well)
    for i in range(len(grid)):
        # Iterate through each column in the well
        for j in range(len(grid[i])):
            # If the current cell is 1, we need to empty it
            if grid[i][j] == 1:
                # Count the number of cells that can be emptied with the current capacity
                bucket_movements += math.ceil(j / capacity)

    return bucket_movements
capacity = 1