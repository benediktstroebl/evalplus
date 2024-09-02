
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
    # Time Complexity: O(N*M)
    # Space Complexity: O(N*M)
    # see https://stackoverflow.com/questions/56320395/
    # see https://www.youtube.com/watch?v=nL9-3QsF6bY
    # see https://www.youtube.com/watch?v=hZ0ExZIxPYo
    rows, cols = len(grid), len(grid[0])
    dist = [[math.inf for _ in range(cols)] for _ in range(rows)]
    dist[0][0] = 0

    for i in range(1, rows):
        if grid[i][0] == 1:
            dist[i][0] = 0
        else:
            dist[i][0] = dist[i-1][0]
    for j in range(1, cols):
        if grid[0][j] == 1:
            dist[0][j] = 0
        else:
            dist[0][j] = dist[0][j-1]

    for i in range(1, rows):
        for j in range(1, cols):
            if grid[i][j] == 1:
                dist[i][j] = min(dist[i-1][j], dist[i][j-1])
            else:
                dist[i][j] = min(dist[i-1][j], dist[i][j-1]) + 1

    return dist[-1][-1]
