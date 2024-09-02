
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

    def dfs(grid, row, col, capacity, times):
        if row >= len(grid):
            return times
        if col >= len(grid[0]):
            return times
        if grid[row][col] == 0:
            return times

        if grid[row][col] > capacity:
            grid[row][col] -= capacity
            return dfs(grid, row, col + 1, capacity, times + 1)
        else:
            grid[row][col] -= capacity
            return dfs(grid, row + 1, col, capacity, times + 1)

    if len(grid) == 0:
        return 0
    if len(grid[0]) == 0:
        return 0

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                capacity = capacity if capacity <= grid[row][col] else grid[row][col]
                count = dfs(grid, row, col, capacity, count)

    return count

