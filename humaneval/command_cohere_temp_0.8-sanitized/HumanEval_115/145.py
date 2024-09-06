import math
def max_fill(grid, capacity) :
    filled_spots = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if row[j] == 1:
                filled_spots += math.ceil(j / capacity)
    return filled_spots