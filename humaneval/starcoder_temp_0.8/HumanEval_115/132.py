
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
    def helper(grid, x, y, rows, cols, capacity, memo):
        if (x, y, capacity) in memo:
            return memo[(x, y, capacity)]

        if capacity == 0:
            return 0
        if x == rows:
            return 0
        if y == cols:
            return helper(grid, x + 1, 0, rows, cols, capacity, memo)

        if grid[x][y] == 1:
            take_capacity = min(capacity, 1)
            fill_well = helper(grid, x, y + 1, rows, cols, capacity - take_capacity, memo)
            no_fill_well = helper(grid, x + 1, y, rows, cols, capacity, memo)
            memo[(x, y, capacity)] = max(fill_well, no_fill_well)
            return memo[(x, y, capacity)]
        else:
            fill_well = helper(grid, x, y + 1, rows, cols, capacity, memo)
            no_fill_well = helper(grid, x + 1, y, rows, cols, capacity, memo)
            memo[(x, y, capacity)] = max(fill_well, no_fill_well)
            return memo[(x, y, capacity)]

    return helper(grid, 0, 0, len(grid), len(grid[0]), capacity, {})

