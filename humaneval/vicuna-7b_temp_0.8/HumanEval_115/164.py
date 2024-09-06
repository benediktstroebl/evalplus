
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
    rows, cols = grid.shape
    # create an empty list to store the number of times buckets are lowered
    num_of_times = [0] * (cols + 1)
    
    # fill the grid with water
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                grid[row][col] = 1
                bucket_index = col * rows + row
                num_of_times[bucket_index] += 1
    
    # fill the grid with water
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                grid[row][col] = 0
    
    # empty the grid with water
    while num_of_times[0] > 0:
        for bucket_index in range(1, cols + 1):
            num_of_times[bucket_index] -= 1
            grid[bucket_index - 1][0] = 0
    
    return num_of_times[cols]