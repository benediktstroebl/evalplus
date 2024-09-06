import math
def max_fill(grid, capacity):
    counter = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if row[j] == 1:
                counter += math.ceil(j / capacity)
    return counter