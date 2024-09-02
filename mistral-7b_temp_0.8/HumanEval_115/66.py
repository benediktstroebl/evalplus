
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

    M, N = len(grid), len(grid[0])

    visited = [[False for _ in range(N)] for _ in range(M)]
    queue = [(0, 0, 0)]

    while queue:
        x, y, level = queue.pop(0)

        if level > capacity:
            continue

        if (x, y) not in visited:
            visited[x][y] = True

            # UP
            if 0 <= x-1 < M and not visited[x-1][y] and grid[x-1][y] == 1:
                queue.append((x-1, y, level+1))

            # RIGHT
            if 0 <= y < N and not visited[x][y+1] and grid[x][y+1] == 1:
                queue.append((x, y+1, level+1))

            # DOWN
            if 0 <= x+1 < M and not visited[x+1][y] and grid[x+1][y] == 1:
