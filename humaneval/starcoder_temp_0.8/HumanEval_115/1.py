
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
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])

    left = [[0 for _ in range(m)] for _ in range(n)]
    right = [[0 for _ in range(m)] for _ in range(n)]

    # initialize boundaries
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                if j == 0:
                    left[i][j] = capacity - 1
                else:
                    left[i][j] = left[i][j - 1]
                if j == m - 1:
                    right[i][j] = capacity - 1
                else:
                    right[i][j] = right[i][j + 1]

    # find longest path
    ans = 0
    for i in range(n):
        for j in range(m):
            if not grid[i][j]:
                continue
            # the length of the path is max(left) + max(right) + 1
            ans = max(ans, left[i][j] + right[i][j] + 1)

    return ans
