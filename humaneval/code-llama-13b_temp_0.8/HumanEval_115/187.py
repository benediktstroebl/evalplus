
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
    
    n_rows = len(grid)
    n_columns = len(grid[0])
    times = 0
    
    while n_rows != 0:
        max_well = 0
        max_well_index = -1
        max_column = 0

        for i in range(n_rows):
            row = grid[i]
            for j in range(n_columns):
                if row[j] > max_well:
                    max_well = row[j]
                    max_well_index = i
                    max_column = j

        grid[max_well_index][max_column] = 0
        n_rows -= 1

        if max_well == 0:
            times += 1
            continue

        if max_well < capacity:
            times += math.ceil(capacity/max_well)
            continue

        times += 1
        max_well -= capacity
        for i in range(n_rows):
            if i != max_well_index:
                grid[i][max_column] += max_well

    return times
