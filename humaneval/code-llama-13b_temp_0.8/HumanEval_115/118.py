
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
    # ------------------------------------------------------------------
    # Diagrammatic Visualisation:
    #   h1 h2 h3 h4
    # v1 0  1  0  0
    # v2 0  1  0  0
    # v3 1  1  1  1
    # v4 0  1  1  1
    # h1: 0  1  2  3
    # h2: 0  1  2  3
    # h3: 0  1  2  3
    # h4: 0  1  2  3
    # h1 + h2 = 1, 2, 2, 3
    # h2 + h3 = 2, 3, 3, 4
    # h3 + h4 = 3, 4, 4, 5
    # ------------------------------------------------------------------
    grid = list(map(lambda x: list(x), grid))
    row_count, col_count = len(grid), len(grid[0])
    empty_count = row_count * col_count
    grid = [
        [i * col_count + j for j in range(1, col_count + 1)]
        for i in range(1, row_count + 1)
    ]
    grid[0][0] = 0
    for i in range(1, row_count):
        grid[i][0] = grid[i - 1][0] + 1
    for j in range(1, col_count):
        grid[0][j] = grid[0][j - 1] + 1
    for i in range(1, row_count):
        for j in range(1, col_count):
            if grid[i][j]:
                grid[i][j] = min(
                    grid[i - 1][j - 1],
                    grid[i - 1][j],
                    grid[i][j - 1],
                ) + 1
    # print('\n'.join([' '.join(map(str, i)) for i in grid]))
    # max_volume = grid[-1][-1]
