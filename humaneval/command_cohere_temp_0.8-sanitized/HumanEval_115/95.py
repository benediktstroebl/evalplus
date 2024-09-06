import math
def max_fill(grid, capacity):
    bucket_fill = 0
    counter = 0
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if row[j] == 1:
                bucket_fill += 1
                if bucket_fill >= capacity:
                    counter += bucket_fill // capacity
                    bucket_fill = 0 
        # Add any remaining water
    if bucket_fill > 0:
        counter += bucket_fill // capacity
    return counter