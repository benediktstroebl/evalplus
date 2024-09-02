
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
    
    # 1. VISIT
    n_rows, n_cols = len(grid), len(grid[0])
    
    def find_well(x, y):
        q = [(x, y)]
        grid[x][y] = 0
        
        while q:
            x, y = q.pop(0)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < n_rows and 0 <= yy < n_cols and grid[xx][yy] == 1:
                    grid[xx][yy] = 0
                    q.append((xx, yy))
    
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                find_well(i, j)
        
    # 2. EXPLORE
    # 3. CALC
