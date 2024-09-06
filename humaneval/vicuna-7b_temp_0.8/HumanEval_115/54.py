
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
    # Preprocessing
    grid_length = grid.length
    grid_width = grid[0].length

    rows = grid_length // grid_width
    columns = grid.length % grid_width

    # Emptying the wells using buckets
    for i in range(0, rows):
        for j in range(0, columns):
            if grid[i][j] == 1:
                if grid[i][j] == 1 and grid[i][j + 1] == 0:
                    bucket_index = j + 1
                else:
                    bucket_index = 0
                bucket_index += 1
                grid[i][j] = 0
                grid[i][bucket_index] = 1
                capacity_left = 0
                while capacity_left > 0:
                    if grid[i + capacity_left][j] == 0:
                        grid[i + capacity_left][j] = 1
                        capacity_left -= 1
                    else:
                        break
    return grid[0][0] + rows - 1