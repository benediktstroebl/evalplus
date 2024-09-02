
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
    grid_size = len(grid)
    well_size = len(grid[0])
    table = [[0 for _ in range(well_size)] for _ in range(grid_size)]

    for row in range(grid_size):
        for col in range(well_size):
            if grid[row][col] == 1:
                table[row][col] = 1

    for row in range(grid_size):
        table[row].sort(reverse=True)

    # if 0, we need to reach the last well
    if table[0][0] == 0:
        return table[0][0]
    else:
        total, index = 0, 1
        while index < well_size:
            current_well = table[0][index]
            next_well = table[0][index + 1]
            if current_well > next_well:
                total += current_well - next_well
                index += 1
            else:
                table[0][index] -= table[0][index + 1]
                index += 2
        return total + max_fill(table, capacity - table[0][0])

