
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
    row_size = max(grid.shape)
    rows = grid.shape[0]
    cols = grid.shape[1]
    
    # Find the rows with water
    water_rows = [i for i, cell in enumerate(grid) if cell == 1]
    
    # Drain the water
    for row in water_rows:
        for i in range(len(row)):
            if row[i] == 1 and (i > 0 and row[i-1] == 1 or i == len(row) - 1 and row[i+1] == 1):
                grid[row[i], row[i-1], row[i+1]] = 0
    
    # Fill the buckets
    used_buckets = set()
    remaining = 0
    while remaining < bucket_capacity * rows:
        # Find the row with the most water to be extracted
        max_water = 0
        max_row = None
        for row in water_rows:
            water = row[max_water]
            if water > max_water:
                max_water = water
                max_row = row[max_water]
        if max_row is None:
            # No more water to extract
            break
        else:
            # Extract water from the row
            for i in range(max_row):
                if grid[max_row, i, max_row] == 1 and grid[i, max_row, max_row] == 0:
                    grid[max_row, i, max_row] = 0
                    remaining += 1
                    used_buckets.add(max_row)
                    if remaining >= bucket_capacity:
                        break
    return used_buckets