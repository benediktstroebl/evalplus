
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
    m = len(grid)
    n = len(grid[0])
    if m == 0:
        return 0
    if n == 0:
        return 0
    # this is a 2D array with all cells representing the water available from each well
    fill = [[0 for col in range(n)] for row in range(m)]
    # fill[i] contains the water available from each well i
    # fill[i][j] contains the water available from well i and column j
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 1:
                fill[row][col] = capacity
    count = 0
    while any(any(row) for row in fill):
        # count the number of times fill needs to be changed
        # fill[i] contains the water available from each well i
        # fill[i][j] contains the water available from well i and column j
        for row in range(m):
            for col in range(n):
                if fill[row][col] > 0:
                    # this is the cell where we are currently looking
                    # we can move to this cell if we have a low water in one of its neighbors
                    fill[row][col] -= 1
                    # move left
                    if col > 0 and fill[row][col-1] < fill[row][col]:
                        fill[row][col-1] = fill[row][col]
                    # move right
                    if col < n-1 and fill[row][col+1] < fill[row][col]:
                        fill[row][col+1] = fill[row][col]
                    # move down
                    if row < m-1 and fill[row+1][col] < fill[row][col]:
                        fill[row+1][col] = fill[row][col]
                    # move up
                    if row > 0 and fill[row-1][col] < fill[row][col]:
                        fill[row-1][col] = fill[row][col]
        count += 1

    return count
