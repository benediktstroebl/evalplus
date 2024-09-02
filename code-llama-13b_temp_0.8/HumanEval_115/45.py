
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
    nb_rows = len(grid)
    nb_cols = len(grid[0])
    def extract_from(i, j):
        # Extract water from well (i,j)
        if i < 0 or i >= nb_rows or j < 0 or j >= nb_cols:
            # Out of the grid
            return 0
        if grid[i][j] == 0:
            # No water
            return 0
        if grid[i][j] == 1:
            # Water
            grid[i][j] = 0
            return 1 + extract_from(i-1, j) + extract_from(i+1, j) + extract_from(i, j-1) + extract_from(i, j+1)
    
    res = 0
    for i in range(nb_rows):
        for j in range(nb_cols):
            res += math.ceil(extract_from(i,j)/capacity)
    return int(res)
