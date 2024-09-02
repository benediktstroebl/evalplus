
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

    row_count = len(grid)
    col_count = len(grid[0])

    previous = [[[-1, math.inf] for _ in range(col_count)] for _ in range(row_count)]

    def dfs(i, j, grid, capacity, bucket_capacity):
        if i < 0 or j < 0 or i >= row_count or j >= col_count or grid[i][j] == 0 or previous[i][j][1] <= bucket_capacity:
            return 0
        
        if previous[i][j][0]!= -1 and previous[i][j][1] <= bucket_capacity:
            return previous[i][j][0]
        
        count = 0
        for p in range(max(0, i-1), min(i+2, row_count)):
            for q in range(max(0, j-1), min(j+2, col_count)):
                count += dfs(p, q, grid, capacity, bucket_capacity-1)
        
        previous[i][j][0] = count
