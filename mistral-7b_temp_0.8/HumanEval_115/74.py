
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
    if not grid or not capacity:
        return 0

    row, col = len(grid), len(grid[0])
    seen = set()
    ans = 0
    queue = []
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                queue.append((i,j,1))
                seen.add((i,j))

    while queue:
        bucket, start_x, start_y = queue.pop()

        for dir_x, dir_y in ((0,1),(0,-1),(1,0),(-1,0)):
            x, y = start_x + dir_x, start_y + dir_y
            if 0 <= x < row and 0 <= y < col and (x,y) not in seen and grid[x][y] == 1:
                queue.append((bucket, x, y))
                seen.add((x,y))
        if bucket < capacity:
            ans += 1
        else:
           
