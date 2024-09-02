
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
    if not grid:
        return 0
    times = 0
    rows = len(grid)
    cols = len(grid[0])
    while True:
        times += 1
        copy = [[None]*cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                copy[row][col] = grid[row][col]

        for row in range(rows):
            if row == 0:
                continue
            for col in range(cols):
                if copy[row-1][col] > 0:
                    copy[row][col] += copy[row-1][col]

        for col in range(cols):
            if col == 0:
                continue
            for row in range(rows):
                if copy[row][col-1] > 0:
                    copy[row][col] += copy[row][col-1]

        flag = False
        for row in range(rows):
            for col in range(cols):
                if copy[row][col] > capacity:
                    flag = True
                    if row == 0:
                        flag = False
                    elif grid[row-1][col] > 0:
                        grid[row-1][col] -= capacity
                    else:
                        flag = False
                    if col == 0:
                        flag = False
                    elif grid[row][col-1] > 0:
                        grid[row][col-1] -= capacity
                    else:
                        flag = False
                    if row == rows - 1:
                        flag = False
                    elif grid[row+1][col] > 0:
                        grid[row+1][col] -= capacity
                    else:
                        flag = False
                    if col == cols - 1:
                        flag = False
                    elif grid[row][col+1] > 0:
                        grid[row][col+1] -= capacity
                    else:
                        flag = False

                    if flag:
                        copy[row][col] = copy[row][col] - capacity
                
