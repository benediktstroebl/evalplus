import math
def max_fill(grid, capacity) :
    filled_wells = 0
    for i in range(len(grid)) :
        row = grid[i]
        bucket_count = 0
        for j in range(len(row)) :
            if row[j] == 1 :
                bucket_count += 1
                if bucket_count == capacity :
                    filled_wells += 1
                    bucket_count = 0
        if bucket_count > 0 :
            filled_wells += bucket_count
    return filled_wells