
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

    wells = []
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        wells += grid[i]
    
    buckets = []
    for i in range(cols):
        buckets.append(capacity)
    
    def fill(wells, buckets, buckets_length, rows, cols, row, col):
        if wells[row] == 0:
            buckets[col] = buckets[col] - 1
            wells[row] = 1
        elif buckets[col] > 0:
            buckets[col] = buckets[col] - 1
            wells[row] = 0
        else:
            return 1
        if row < rows - 1:
            return fill(wells, buckets, buckets_length, rows, cols, row+1, col)
        elif col < cols - 1:
            return fill(wells, buckets, buckets_length, rows, cols, row, col+1)
        else:
            return 0
    
    return fill(
