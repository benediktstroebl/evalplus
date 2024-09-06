
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
    visited = [[False for _ in range(n)] for _ in range(m)]
    q = [[0, 0, 0]] # (row, col, water)
    rows, cols = set(), set()
    res = 0

    while q:
        row, col, water = q.pop(0)
        visited[row][col] = True
        rows.add(row)
        cols.add(col)
        for i in range(4):
            rr, cc = row + d_x[i], col + d_y[i]
            if 0 <= rr < m and 0 <= cc < n and not visited[rr][cc] and grid[rr][cc] == 1:
                if rr not in rows and cc not in cols:
                    q.append([rr, cc, water + 1])
                elif water + 1 < capacity:
                    q.append([rr, cc, water + 1])

        if water >= capacity:
