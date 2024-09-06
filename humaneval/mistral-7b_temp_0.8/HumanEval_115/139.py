
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
    # your code here
    # https://www.geeksforgeeks.org/maximum-number-of-wells-that-can-be-filled-with-the-bucket/
    n, m = len(grid), len(grid[0])
    l = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                l.append((i, j))
    visited = [[0] * m for _ in range(n)]
    ans = 0
    while l:
        (x, y) = l.pop()
        visited[x][y] = 1
        if x - 1 >= 0 and visited[x - 1][y] == 0 and grid[x - 1][y] == 1:
            visited[x - 1][y] = 1
            l.append((x - 1, y))
        if x + 1 < n and visited[x + 1][y] == 0 and grid[x + 1][y] == 1
