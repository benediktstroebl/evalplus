
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

    ret = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                ret += c >= capacity
                continue
            dp = numpy.zeros((capacity+1, c+1), dtype=bool)
            for i in range(1, c+1):
                dp[i, i] = True
            for i in range(c, -1, -1):
                for j in range(i, c, -1):
                    dp[i, j] = dp[i, j-1] and \
                               (grid[r][c-i] <= grid[r][c-j] and \
                                dp[i+int(math.ceil((j-i)/2)), j+int(math.ceil((j-i)/2))])
            for i in range(1, capacity+1):
                if dp[i, c]:
                    ret += 1

            for j in range(1, c+1):
                dp[i, j] = False
                dp[i, j] = True

    return ret

