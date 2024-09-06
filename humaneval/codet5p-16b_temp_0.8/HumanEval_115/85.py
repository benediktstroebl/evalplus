
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

    m = len(grid)
    n = len(grid[0])

    def fill_wells(grid, capacity):
        buckets = [[capacity for _ in range(n)] for _ in range(m)]
        steps = fill_wells_helper(grid, buckets, 0, 0, capacity)
        return steps

    def fill_wells_helper(grid, buckets, i, j, capacity):
        if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == 0:
            return 0
        if i == m - 1 and j == n - 1:
            return 1
        buckets[i][j] -= 1
        if buckets[i][j] == 0:
            return 0
        
        steps = 0
        if i + 1 < m:
            steps += fill_wells_helper(grid, buckets, i + 1, j, capacity)
        if j + 1 < n:
            steps += fill_wells_helper(grid, buckets, i, j + 1, capacity)

        buckets[i][j
