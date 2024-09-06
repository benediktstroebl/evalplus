
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
    # This is a slight variant on the solution for the house water problem
    rows = len(grid)
    cols = len(grid[0])
    moves = 0
    left = cols
    right = 0
    while True:
        row = -1
        for i in range(rows):
            for j in range(left, right+1):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    row = i
                    break
            if row != -1:
                break
        if row == -1:
            break
        for j in range(right+1, cols):
            if grid[row][j] == 1:
                grid[row][j] = 0
                right += 1
                break
        for j in range(left-1, -1, -1):
            if grid[row][j] == 1:
                grid[row][j] = 0
                left -= 1
                break
        moves += 1
    return moves
