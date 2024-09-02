
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

    def empty_well(grid, capacity, row, col):
        def dfs(grid, capacity, row, col):
            if row >= m or row < 0 or col >= n or col < 0:
                return 0
            if grid[row][col] == 1:
                return 1
            grid[row][col] = 1
            return dfs(grid, capacity, row + 1, col) + dfs(grid, capacity, row, col + 1) + dfs(grid, capacity, row, col - 1) + dfs(grid, capacity, row - 1, col)
        return dfs(grid, capacity, row, col)

    def max_fill(grid, capacity):
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                count += empty_well(grid, capacity, i, j)
        return count

    count = max_fill(grid, capacity)
    for i in
