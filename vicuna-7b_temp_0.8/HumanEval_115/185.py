
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
    N = grid.length
    M = grid[:,1].length
    WELLS = [[0]*(N+1) for _ in range(M+1)]
    for i in range(M+1):
        WELLS[i][0] = i
    for j in range(N+1):
        WELLS[0][j] = j
    for row in WELLS:
        print(row)
        for i in range(1, N+1):
            for j in range(M+1):
                if grid[i-1][j-1] == 1:
                    if WELLS[i-1][j] < grid[i-1][j]:
                        return grid[i-1][j]
    return 0
