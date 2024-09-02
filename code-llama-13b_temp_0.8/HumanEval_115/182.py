
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
    # try solving using max_fill
    
    # first attempt
    rows = len(grid)
    cols = len(grid[0])
    if rows == 1:
        return cols
    elif cols == 1:
        return rows
    fill = [[0 for _ in range(cols)] for _ in range(rows)]
    fill[0][0] = grid[0][0]
    fill[0][1] = grid[0][1] + grid[0][0]
    fill[1][0] = grid[1][0] + grid[0][0]
    fill[1][1] = max(grid[0][1], grid[1][1])
    for i in range(2, rows):
        fill[i][0] = grid[i][0] + fill[i-1][0]
        for j in range(1, cols):
            fill[i][j] = max(fill[i-1][j], grid[i][j] + fill[i][j-1])
    #print(fill)
    bucket = capacity
    for i in range(rows):
        for j in range(cols):
            if fill[i][j] > bucket:
                bucket = fill[i][j]
                break
        if bucket == capacity:
            break
    count = 0
    while True:
        temp = bucket
        bucket -= capacity
        count += 1
        for i in range(rows):
            for j in range(cols):
                if fill[i][j] == temp:
                    if i == rows-1 and j == cols-1:
                        return count
                    elif i == rows-1:
                        fill[i][j] = fill[i][j-1]
                    elif j == cols-1:
                        fill[i][j] = fill[i-1][j]
                    else:
                        fill[i][j] = max(fill[i-1][j], fill[i][j-1])
                    break
            if fill[i][j] < bucket:
                bucket = fill[i][j]
                break
        if bucket == temp:
            return -1
