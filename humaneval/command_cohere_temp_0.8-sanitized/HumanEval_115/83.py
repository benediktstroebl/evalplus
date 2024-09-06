import math
def max_fill(grid, capacity):
    empty_counter = 0
    total_counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                empty_counter += 1
            else:
                total_counter += 1
        if empty_counter > 0:
            return total_counter // empty_counter
    return total_counter