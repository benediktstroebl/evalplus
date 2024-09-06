import math
def max_fill(grid, capacity):
    filled_wells = 0
    for i in range(len(grid)):   # loop through each row
        row = grid[i]
        bucket_fill = 0
        for j in range(len(row)): # loop through each column
            if row[j] == 1:
                bucket_fill += 1
                if bucket_fill == capacity:
                    filled_wells += 1
                    bucket_fill = 0
        if bucket_fill > 0:
            filled_wells += bucket_fill
    
    return filled_wells
capacity = 1