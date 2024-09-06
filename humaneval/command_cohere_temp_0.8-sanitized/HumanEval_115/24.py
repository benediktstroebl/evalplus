import math
def max_fill(grid, capacity):
    """
    Determine the maximum amount of water that can be extracted from a grid of wells.
    """
    # Calculate the maximum water that can be stored in each row
    row_max = [max(row) for row in grid]
    
    # Calculate the cumulative sum of rows
    cs_row = [0] * len(grid[0])
    for i in range(len(grid)):
        cs_row.extend(cs_row[len(grid[i])-1:] + grid[i])
    
    # Initialize result and count of how many times the bucket is lowered
    result = 0
    bucket_lower = 0
    
    # Iterate from the end of the grid to the start to avoid overflow
    for i in range(len(cs_row)-1, -1, -1):
        # If the capacity is greater than the amount of water in the current row,
        # empty the entire row and move to the previous row
        if cs_row[i] > capacity:
            result += row_max[i]
            bucket_lower += 1
            cs_row[i] = 0
        # If the capacity is equal to the amount of water in the current row,
        # empty the capacity amount of water and move to the previous row
        elif cs_row[i] == capacity:
            result += capacity
            bucket_lower += 1
            cs_row[i] = 0
        # If the capacity is less than the amount of water in the current row,
        # empty the maximum capacity in this row and move to the previous row
        else:
            result += capacity
            bucket_lower += 1
            cs_row[i] -= capacity
    
    return result, bucket_lower