
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

    rows = len(grid)
    cols = len(grid[0])
    res = math.inf
    print(rows, cols)
    def helper(grid, i, j, row, col, capacity, visited):
        nonlocal res
        if i == rows - 1 and j == cols - 1:
            return 0
        if capacity < 0:
            return math.inf
        if (i,j) in visited:
            return math.inf
        visited.add((i,j))
        curr = grid[i][j]
        if curr == 0:
            return math.inf
        if curr == 1:
            res = min(res, helper(grid, i + 1, j, row, col, capacity - 1, visited))
            res = min(res, helper(grid, i, j + 1, row, col, capacity - 1, visited))
            res = min(res, helper(grid, i, j - 1, row, col, capacity - 1, visited))
            res = min(res, helper(grid, i - 1, j, row,
