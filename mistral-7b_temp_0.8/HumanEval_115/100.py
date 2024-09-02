
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

    if not grid or not grid[0]:
        return 0

    # inizialize the matrix with the same dimension of the grid
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    # inizialize the queue with the first element of the grid
    queue = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                queue.append((r, c))

    # while the queue is not empty, we process the element at the front of the queue,
    # i.e. the water we can extract from the well
    while queue:
        r, c = queue.pop(0)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newr, newc = r + dr, c + dc
            if not (0 <= newr < len(grid) and 0 <= newc < len(grid[newr]))
