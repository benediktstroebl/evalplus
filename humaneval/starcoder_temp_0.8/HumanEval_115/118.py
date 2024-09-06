
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
    if not grid:
        return 0
    # get number of columns and rows
    rows = len(grid)
    columns = len(grid[0])
    # get total capacity of all wells
    total_cap = 0
    for row in grid:
        for column in row:
            if column == 1:
                total_cap += 1
    if total_cap <= capacity:
        return 0
    # total capacity can be filled in rows
    # try all possible combinations of buckets
    options = []
    for i in range(rows):
        options.append([])
        for j in range(columns):
            if grid[i][j] == 1:
                options[i].append(j)
    print(options)
    # combine options to get all possible combinations
    # all_options = [[]]
    # for row in options:
    #     for column in row:
    #         for option in all_options:
    #             option.append(column)
    #         all_options.append(row)
    # print(all_options)
    all_options = list(itertools.product(*options))
    print(all_options)
    # fill the buckets
    filled_buckets = 0
    for option in all_options:
        temp_cap = 0
        for column in option:
            for row in grid:
                if row[column] == 1:
                    temp_cap += 1
        if temp_cap > capacity:
            filled_buckets += 1
    return filled_buckets

