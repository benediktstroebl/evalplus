import math
def max_fill(grid, capacity) :
    filled_spots = 0
    for i in range(len(grid)) :
        row = grid[i]
        bucket = 0
        for j in range(len(row)) :
            if row[j] == 1 :
                filled_spots += bucket
                bucket = 0
                if capacity > 0 :
                    capacity -= 1
                    bucket += 1
            else:
                bucket += 1
        filled_spots += bucket
    return filled_spots
capacity = 1