
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
    # your code goes here
    n = len(grid)
    m = len(grid[0])
    water = 0
    seen = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and (i,j) not in seen:
                water += min(capacity, grid[i][j])
                seen.add((i,j))
                for k in range(capacity):
                    if i > 0:
                        seen.add((i-1,j))
                        grid[i-1][j] -= min(1, grid[i][j])
                    if i < n-1:
                        seen.add((i+1,j))
                        grid[i+1][j] -= min(1, grid[i][j])
                    if j > 0:
                        seen.add((i,j-1))
                        grid[i][j-1] -= min(1, grid[i][j])
                    if j < m-1:
