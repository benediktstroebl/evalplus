
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
    n, m = len(grid), len(grid[0])
    # Water on each column
    water_on_column = [0] * m
    # Maximum water on each column
    max_water_on_column = [0] * m

    # Fill water on each column
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                water_on_column[j] += 1

    # Fill maximum water on each column
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                # Update maximum water
                max_water_on_column[j] = max(max_water_on_column[j], water_on_column[j])
            # Update water
            else:
                water_on_column[j] = 0

    # print(water_on_column, max_water_on_column)
    # Find columns with water
    columns_with_water = []
    for i in range(m):
        if max_water_on_column[i]:
            columns_with_water.append(i)
    # print(columns_with_water)
    # Calculate minimum water
    minimum_water = 0
    for i in range(len(columns_with_water) - 1):
        minimum_water += math.ceil((columns_with_water[i + 1] - columns_with_water[i]) / bucket_capacity)
    return minimum_water



