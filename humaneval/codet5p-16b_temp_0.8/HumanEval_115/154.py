
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

    m, n = len(grid), len(grid[0])
    rows, cols = [], []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                rows.append(i)
                cols.append(j)
    buckets = {(i,j) : capacity for i in range(m) for j in range(n) if grid[i][j] == 1}
    bucket_filled = 0
    count = 0
    while buckets:
        bucket_filled += 1
        temp = []
        for r, c in buckets.keys():
            if r in rows and c in cols:
                new_r, new_c = r+rows[rows.index(r)+1], c+cols[cols.index(c)+1]
                if new_r < m and new_c < n:
                    if grid[new_r][new_c] == 1:
                        temp.append((new_r, new_c))
        count += len(temp)
        for r
