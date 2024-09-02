
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
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    def BFS(row, col):
        from collections import deque
        nonlocal grid
        visited[row][col] = True
        q = deque()
        q.append((row, col))
        while q:
            row, col = q.popleft()
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for r, c in directions:
                if row+r < 0 or row+r >= rows or col+c < 0 or col+c >= cols or visited[row+r][col+c] == True or grid[row+r][col+c] == 0:
                    continue
                visited[row+r][col+c] = True
                grid[row+r][col+c] = 0
                q.append((row+r, col+c))
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                visited[i][j] = True
            if grid[i][j] == 1:
                BFS(i, j)
                count += 1
    return count
