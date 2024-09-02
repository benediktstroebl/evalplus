
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

    height, width = len(grid), len(grid[0])
    visited = [[False for _ in range(width)] for _ in range(height)]

    if grid == [[0]*width for _ in range(height)]:
        return 0

    def dfs(i, j, dist):
        if i < 0 or j < 0 or i >= height or j >= width or visited[i][j] or grid[i][j] == 0:
            return 0

        visited[i][j] = True
        filled = 0
        for d in range(4):
            i1, j1 = i + dy[d], j + dx[d]
            if grid[i1][j1] == 1:
                filled = max(filled, dfs(i1, j1, dist + 1))
        return filled

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    max_filled = 0
    for i in range(height):
       
