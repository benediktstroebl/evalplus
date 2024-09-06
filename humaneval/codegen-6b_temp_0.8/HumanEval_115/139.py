
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
    cols = len(grid[0])

    def getWater(grid, c):
        row = rows - 1
        col = 0
        waterDrained = 0
        while(row >= 0 and col < cols):
            if grid[row][col] > 0:
                waterDrained += min(grid[row][col], c)
                grid[row][col] -= grid[row][col]
                col += 1
            else:
                row -= 1
        
        if col == cols:
            return waterDrained
        else:
            return -1
    
    for row in range(rows):
        if grid[row][0] == 1:
            return -1
    def getMaxCap(grid, c):
        row = rows - 1
        col = 0
        waterDrained = 0
        while(row >= 0 and col < cols):
            if grid[row][col] > 0:
                if grid[row][col] < c:
                    waterDrained += c - grid[row][col]
                    grid[row][col] = 0
                else:
                    waterDrained += grid[row][col]
                    grid[row][col] = 0
                    row -= 1
                    continue
            else:
                row -= 1
        
        if col == cols:
            return waterDrained
        else:
            return -1
    
    cols = len(grid[0])
    while(True):
        leftCap = capacity
        for row in range(rows - 1, -1, -1):
            if leftCap > 0:
                maxCap = getMaxCap(grid, leftCap)
                if maxCap != -1:
                    leftCap = maxCap
            elif row == 0:
                if leftCap == 0:
                    break
                else:
                    return -1
    return -1
