
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

    well_num = grid[0].count(1)
    row_num = len(grid)
    column_num = len(grid[0])
    grid_area = row_num * column_num
    max_fill_capacity = math.floor(grid_area / well_num)

    if capacity >= max_fill_capacity:
        return 1

    for row in grid:
        if row.count(1) == 0:
            grid.remove(row)

    row_num = len(grid)
    column_num = len(grid[0])
    grid_area = row_num * column_num
    max_fill_capacity = math.floor(grid_area / well_num)

    if capacity >= max_fill_capacity:
        return 1

    row_index = 0
    column_index = 0
    direction_index = 0
    direction = [
        {'row_change': 1, 'column_change': 0},
        {'row_change': 0, 'column_change': 1},
        {'row_change': -1, 'column_change': 0},
        {'row_change': 0, 'column_change': -1},
    ]
    current_capacity = capacity
    bucket_lowers = 0

    while True:
        if grid[row_index][column_index] == 0:
            direction_index = (direction_index + 1) % 4
            direction_change = direction[direction_index]
            row_index += direction_change['row_change']
            column_index += direction_change['column_change']
            continue

        grid[row_index][column_index] = 0
        current_capacity += 1
        if current_capacity == max_fill_capacity:
            current_capacity = capacity
            bucket_lowers += 1
            direction_index = (direction_index + 1) % 4
            direction_change = direction[direction_index]
            row_index += direction_change['row_change']
            column_index += direction_change['column_change']
