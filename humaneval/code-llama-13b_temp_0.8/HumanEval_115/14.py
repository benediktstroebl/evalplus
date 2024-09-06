
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    def fill(row, bucket_capacity):
        # Fill the current row from left to right
        # Return the number of buckets filled
        filled = 0
        for i in range(len(row)):
            if row[i] == 0:
                continue
            bucket_capacity -= 1
            row[i] = 0
            if bucket_capacity == 0:
                break
            row[i+1] += 1
            if i+1 < len(row) and row[i+1] > 0:
                filled += fill(row, bucket_capacity)
            else:
                filled += 1
        return filled
    
    # Count the buckets needed to fill the wells
    buckets = 0
    for row in grid:
        buckets += fill(row, capacity)
    return buckets

