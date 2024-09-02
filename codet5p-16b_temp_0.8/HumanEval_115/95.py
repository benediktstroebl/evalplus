
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

    if not grid: return 0
    n,m = len(grid), len(grid[0])
    p_grid = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                p_grid[i][j] = 1
            else:
                p_grid[i][j] = 0

    q = []
    for i in range(n):
        for j in range(m):
            if p_grid[i][j] == 1:
                q.append((i,j))

    count = 0
    while q:
        u,v = q.pop(0)
        for x,y in [(u-1,v), (u+1,v), (u,v-1), (u,v+1)]:
            if 0<=x<n and 0<=y<m:
                if p_grid[x][y] == 0:
                    p_grid[x][y] = 1
                    count += 1
