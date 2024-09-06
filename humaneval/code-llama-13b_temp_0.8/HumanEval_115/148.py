
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
    rows = len(grid)
    columns = len(grid[0])
    low_sum = 0
    for row in range(0, rows):
        low_sum += grid[row][columns-1]
    low_sum *= capacity
    #print(low_sum)
    for col in range(columns-1, -1, -1):
        low_sum -= min(grid[rows-1][col]*capacity, low_sum)
        #print(low_sum)
        for row in range(rows-1, -1, -1):
            if col+1 < columns:
                low_sum += grid[row][col]*capacity
            low_sum -= min(grid[row][col]*capacity, low_sum)
            #print(low_sum)
    return int(math.ceil(low_sum/(capacity*rows)))

