
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


    # Replace this code with your own code
    
    total_buckets = 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    max_levels = 0
    
    # 1. Get the maximum level of the grid
    for i in range(rows):
        max_levels = max(max_levels, max(grid[i]))
    
    # 2. Create the water levels
    water_levels = [0 for _ in range(max_levels + 1)]
    
    # 3. Fill the water levels
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]:
                water_levels[grid[i][j]] += 1
    
    # 4. Add all the water from all the buckets into the grid
    for i in range(max_levels):
        current_water = water_levels[i]
        for j in range(current_water):
            if water_levels[i]:
