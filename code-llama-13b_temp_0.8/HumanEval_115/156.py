
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
    buckets_capacity = capacity
    well_length = len(grid[0])
    wells_length = len(grid)
    columns = []
    counter = 0
    for row in grid:
        for column in row:
            columns.append(column)
    counter = 0
    while columns:
        for index in range(well_length):
            if columns[index] == 1:
                counter += 1
        if counter > buckets_capacity:
            num_of_iterations = math.ceil(counter / buckets_capacity)
            counter = num_of_iterations * buckets_capacity
        else:
            num_of_iterations = 1
        if columns[0] == 1:
            counter -= num_of_iterations
        columns = columns[well_length:]
    return counter
