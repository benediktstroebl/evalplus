
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
    import math
    rows, cols = len(grid), len(grid[0])
    vol = rows * cols * capacity

    from collections import defaultdict

    dp = defaultdict(int)
    #DP[(r, c)] = dp here, we store the last time we filled a bucket
    # so we only need to store the last row and last column
    # for that bucket

    # row, col
    dp[(0,0)] = grid[0][0]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                dp[(r+1,c)] = max(dp[(r+1,c)], dp[(r,c)] + grid[r][c])
            else:
                dp[(r+1,c)] = dp[(r+1,c)]
                dp[(r,c+1)] = dp[(r,c)] + grid[r][c]

    print(dp)
    return math.ceil(vol/capacity)

input1 = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
input2 = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
input3 = [[0,0,0], [0,0,0]]
input4 = [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
input5 = [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1