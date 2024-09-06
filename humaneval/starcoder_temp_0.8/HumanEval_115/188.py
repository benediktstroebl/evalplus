
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
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                return -1

    water = 0
    filled_wells = set()

    for row in range(rows):
        for col in range(cols):
            if (row, col) in filled_wells:
                continue

            if grid[row][col] == 0:
                continue

            if grid[row][col] == 1:
                water += 1

            bucket_capacity = math.inf

            for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c = row + d_row, col + d_col
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    continue
                if grid[r][c] == 0:
                    continue

                if grid[r][c] == 1:
                    bucket_capacity = min(bucket_capacity, grid[r][c])

            while water > 0 and bucket_capacity > 0:
                water -= bucket_capacity
                bucket_capacity -= 1

            filled_wells.add((row, col))

    return water
