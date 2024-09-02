
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
    def fill_one(row, capacity):
        if grid[row][0] == 1:
            grid[row][0] = 0
            grid[row][1] = 1
            return 1
        for i in range(1, len(row)):
            if grid[row][i] == 1:
                grid[row][i] = 0
                return 1
        return 0
    
    def fill_all(grid, capacity):
        if fill_one(0, capacity) == 1:
            return fill_all(grid, capacity)
        for i in range(1, len(grid)):
            if fill_one(i, capacity) == 1:
                return fill_all(grid, capacity)
        return 0
    
    if fill_all(grid, capacity) == 1:
        return fill_all(grid, capacity)
    else:
        return max(fill_one(0, capacity) + fill_one(1, capacity) + fill_one(2, capacity) + ... + fill_one(len(grid)-1, capacity), (len(grid)-1) * fill_all(grid, capacity))

grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
grid = [[0,0,0,0], [0,0,0,0]]
grid = [[0,0,0]]