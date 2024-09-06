
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
    # import math
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    # print(grid)
    filled_wells = [[-1 for _ in range(cols)] for _ in range(rows)]
    fill_cnt = 0
    while True:
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and filled_wells[row][col] == -1:
                    can_fill = True
                    for adj_row in range(row, -1, -1):
                        if filled_wells[adj_row][col] == -1:
                            continue
                        else:
                            if (
                                filled_wells[row][col]
                                + filled_wells[adj_row][col]
                                + 1
                            ) > capacity:
                                can_fill = False
                            break
                    for adj_row in range(row + 1, rows):
                        if filled_wells[adj_row][col] == -1:
                            continue
                        else:
                            if (
                                filled_wells[row][col]
                                + filled_wells[adj_row][col]
                                + 1
                            ) > capacity:
                                can_fill = False
                            break
                    for adj_col in range(col, -1, -1):
                        if filled_wells[row][adj_col] == -1:
                            continue
                        else:
                            if (
                                filled_wells[row][col]
                                + filled_wells[row][adj_col]
                                + 1
                            ) > capacity:
                                can_fill = False
                            break
                    for adj_col in range(col + 1, cols):
                        if filled_wells[row][adj_col] == -1:
                            continue
                        else:
                            if (
                                filled_wells[row][col]
                                + filled_wells[row][adj_col]
                                + 1
                            ) > capacity:
                                can_fill = False
                            break
                    if can_fill:
                        filled_wells[row][col] = 0
                        fill_cnt += 1
        # print(fill_cnt, filled_wells)
        if fill_cnt == 0:
            break
        else:
            fill_cnt = 0
    return math.ceil(rows * cols / capacity)

