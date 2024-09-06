
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
    def dfs(row, col, grid, capacity):
        nonlocal max_fill

        max_fill = max(max_fill, grid[row][col])

        if capacity == 0:
            return
        elif capacity < 0:
            return
        elif row == len(grid) - 1 and col == len(grid[0]) - 1:
            return

        # fill one cell
        grid[row][col] = 0
        dfs(row, col+1, grid, capacity - 1)
        dfs(row+1, col, grid, capacity - 1)

        # empty one cell
        dfs(row, col+1, grid, capacity)
        dfs(row+1, col, grid, capacity)

        # fill one cell
        grid[row][col] = 1
        dfs(row, col+1, grid, capacity - 1)
        dfs(row+1, col, grid, capacity - 1)

        # empty one cell
        grid[row][col] = 0
        dfs(row, col+1, grid, capacity)
        dfs(row+1, col, grid, capacity)


    grid = [[1,0,1],[1,1,1]]
    capacity = 2

    max_fill = 0
    dfs(0,0, grid, capacity)
    return max_fill




