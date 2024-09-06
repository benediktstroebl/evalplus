
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

    rows, columns = len(grid), len(grid[0])
    # print(grid, capacity)
    
    result = 0
    max_water = 0
    while max_water < capacity:
        max_water = 0
        result += 1
        # print(result, max_water)
        for i in range(rows):
            for j in range(columns):
                water_in_well = grid[i][j]
                # print(water_in_well)
                if water_in_well > 0:
                    max_water_row = 0
                    max_water_col = 0
                    for k in range(columns):
                        max_water_row += grid[i][k]
                    for k in range(rows):
                        max_water_col += grid[k][j]
                    # print(max_water_row, max_water_col)
                    max_water = max(max_water_row, max_water_col)
                    max_water -= water_in_well
                    # print(max_water)
                else:
                    max_water = 0
                    break
        # print(max_water)

    return result
