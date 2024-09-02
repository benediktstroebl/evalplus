
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
    # each grid row can store the number of units of water
    # one well can store 1 unit
    row_cap = [capacity for _ in range(len(grid[0]))]

    # no water in well
    if sum(grid[0]) == 0:
        return 0

    # find first row with non 0 element
    # that row's well store all other rows' usable capacity
    row = 0
    while row < len(grid):
        if row_cap[0] == 0:
            return 0
        if grid[row][0] == 1:
            row_cap[0] -= 1
        else:
            row_cap[0] = row_cap[0] - grid[row][0]
        row += 1

    # iterate through rest of the rows
    # if non 0 element in last row, that row can't store
    # enough water to fill all wells
    row = 1
    while row < len(grid):
        if grid[row][0] == 0:
            return 0
        if row_cap[0] < grid[row][0]:
            return 0
        row_cap[0] -= grid[row][0]
        row += 1

    print(row_cap)
    # remaining water in well can be filled
    return row - 1


grid = [[0]]
cap = 5