
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
    n = len(grid)
    m = len(grid[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            if j == 0:
                dp[i][j] = dp[i-1][j]
            if j == m - 1:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            dp[i][j] += grid[i][j]
    return math.ceil(dp[n-1][m-1] / capacity)

assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5
assert max_fill([[0,0,0], [0,0,0]], 5) == 0
assert max_fill([[0,0,0], [0,0,0]], 0) == 0
assert max_fill([[0,0,0], [0,0,0]], 1) == 1
assert max_fill([[0,0,0], [0,0,0]], 2) == 0
assert max_fill([[0,0,0], [0,0,0]], 3) == 1
assert max_fill([[0,0,0], [0,0,0]], 4) == 0
assert max_fill([[0,0,0], [0,0,0]], 5) == 1
assert max_fill([[0,0,0], [0,0,0]], 6) == 0
assert max_fill([[0,0,0], [0,0,0]], 7) == 1
assert max_fill([[0,0,0],