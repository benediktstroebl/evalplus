
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
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #   A very good way to improve performance is to check   #
    #       if the well is full before trying to fill it.     #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
    # find full wells
    full_wells = []
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == capacity:
                full_wells.append([row, col])
    # fill full wells
    for [row, col] in full_wells:
        counter += 1
        if row - 1 >= 0:
            grid[row-1][col] = min(grid[row-1][col] + grid[row][col], capacity)
        if row + 1 < rows:
            grid[row+1][col] = min(grid[row+1][col] + grid[row][col], capacity)
        if col - 1 >= 0:
            grid[row][col-1] = min(grid[row][col-1] + grid[row][col], capacity)
        if col + 1 < cols:
            grid[row][col+1] = min(grid[row][col+1] + grid[row][col], capacity)
        grid[row][col] = 0
    # bucket capacity exceeded
    while max(map(max, grid)) >= capacity:
        counter += 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == capacity:
                    full_wells.append([row, col])
        for [row, col] in full_wells:
            counter += 1
            if row - 1 >= 0:
                grid[row-1][col] = min(grid[row-1][col] + grid[row][col], capacity)
           
