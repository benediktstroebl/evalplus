
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
    import math
    
    ROWS, COLS = len(grid), len(grid[0])
    water_buckets = [[0] * COLS for _ in range(ROWS)]
    ret = 0
    for row_idx in range(ROWS):
        for col_idx in range(COLS):
            if grid[row_idx][col_idx] == 0:
                continue
            
            # find shortest path from (row_idx, col_idx) to well
            dist, path = dijkstra(grid, (row_idx, col_idx), capacity)
            if len(path) == 0:
                return ret
            
            idx = path.index((row_idx, col_idx))
            water_buckets[row_idx][col_idx] = idx
            ret += len(path) - idx - 1

    for row_idx in range(ROWS):
        for col_idx in range(COLS):
            if grid[row_idx][col_idx] == 1:
                continue

            # remove water from 1 cell
            water = grid[row_idx][col_idx]
            water_buckets[row_idx][col_idx] -= 1
            ret += water

            # empty the well by reducing capacity
            capacity -= min(water, capacity)
            if capacity < 0:
                return -1

    return ret
