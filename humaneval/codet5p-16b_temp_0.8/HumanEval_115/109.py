
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

    if len(grid) == 0:
        return 0

    if len(grid[0]) == 0:
        return 0

    bucket_capacity = capacity
    row_count = len(grid)
    col_count = len(grid[0])

    bucket_count = 0
    water_count = 0
    for row in grid:
        water_count += row.count(1)

    while (water_count > 0):
        for row in grid:
            for col in row:
                if col == 1:
                    row_index = grid.index(row)
                    row_index_end = row_index + 1
                    for row_index_end_row in grid[row_index_end:]:
                        if row_index_end_row[col_count-1] == 1:
                            row_index_end_row[col_index] = 0
                            water_count += 1
                    break
        bucket_count += 1

    return bucket_count

