
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
    visited = [[0]*n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and grid[i][j] == 1:
                queue = [(i, j)]
                visited[i][j] = 1
                
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        x1, y1 = x+dx, y+dy
                        if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
                            continue
                        if not visited[x1][y1] and grid[x1][y1] == 1:
                            visited[x1][y1] = 1
                            queue.append((x1, y1))
                count += 1
    
