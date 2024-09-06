
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
    grid = set(grid)
    rows, cols = grid.maxsize, grid.maxsize
    rows, cols = map(int, (rows//cols, cols//rows))
    grid_new = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                water = grid[row][col]
                grid_new[row][col] = water
                for i in range(col):
                    for j in range(row):
                        if grid[j][i] == 1:
                            grid_new[j][i] = grid_new[j][i] + grid_new[row][col]
    grid_new = set(grid_new)
    for row in range(rows):
        if grid_new[row][cols-1] > capacity:
            # 
            max_times_lower = math.ceil((grid_new[row][cols-1] - capacity) / (grid_new[row][cols-2] + grid_new[row][cols-3])) + 1
            print(max_times_lower)
    return grid_new