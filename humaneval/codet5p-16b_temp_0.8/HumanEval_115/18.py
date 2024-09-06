
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

    def dfs(grid, row, col, capacity):
        # base case
        if row == len(grid) or col == len(grid[0]):
            return math.inf

        grid[row][col] = 0 # set current bucket to empty

        max_water = min(dfs(grid, row+1, col, capacity), dfs(grid, row, col+1, capacity)) # find max water that can be extracted from bucket
        max_water += grid[row][col] # add water in current bucket to max_water

        return max_water

    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    return dfs(grid, 0, 0, capacity)
