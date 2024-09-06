
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

    def helper(grid, capacity, bucket_capacity):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        row_arr = [0 for _ in range(n)]
        col_arr = [0 for _ in range(n)]
        row_max = [0 for _ in range(m)]
        col_max = [0 for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_arr[j] += 1
                    col_arr[j] += 1
                    row_max[i] = max(row_max[i], row_arr[j])
                    col_max[i] = max(col_max[i], col_arr[j])
        def max_fill_helper(i, j, grid, capacity, bucket_capacity):
            if i >= m or i < 0 or j >= n or j < 0:
                return 0
            
