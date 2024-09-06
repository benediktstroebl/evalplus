import math
def max_fill(grid, capacity):
    filled_buckets = 0
    for i in range(len(grid)):   # iterate through each row
        row = grid[i]
        for j in range(len(row)): # iterate through each column in the row
            if row[j] == 1:      # if there's water in the well
                filled_buckets += math.ceil(j / capacity)   # count how many buckets needed
        
        # add extra count if the last column isn't fully filled
        if (j + 1) % capacity != 0:
            filled_buckets += 1

    return filled_buckets