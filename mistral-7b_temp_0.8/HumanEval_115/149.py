
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
    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    q = [(0, 0, 1)]

    while q:
        x, y, cnt = q.pop()

        if (x,y) in visited:
            continue

        visited.add((x,y))

        if cnt == capacity:
            continue

        for i in range(1, cols):
            if grid[x][y+i] == 1:
                q.append((x, y+i, cnt+1))

        for j in range(1, rows):
            if grid[x+j][y] == 1:
                q.append((x+j, y, cnt+1))

        for i in range(1, rows):
            for j in range(1, cols):
                if grid[x+i][y+j] == 1:
                    q.append((x+i, y+j, cnt+1))


    return len(visited)

