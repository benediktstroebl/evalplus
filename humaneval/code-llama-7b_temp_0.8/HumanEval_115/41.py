
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
    N = len(grid)
    if N == 0:
        return 0
    M = len(grid[0])
    if M == 0:
        return 0

    if capacity > M:
        capacity = M

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                grid[i][j] = 0
            else:
                grid[i][j] = capacity

    result = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                continue
            else:
                result += 1
                for k in range(i, N):
                    if grid[k][j] > 0:
                        grid[k][j] -= 1
                    if grid[k][j] == 0:
                        break
    return result
