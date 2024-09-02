
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
    # 1. preprocess the grid
    # 2. start from first row and check if we can empty the well
    # 3. if so, empty well by adding the contents to the bucket
    # 4. after we empty the well, move to the next row and check the same
    # process for each row.

    n = len(grid)
    m = len(grid[0])
    capacity = int(capacity)
    if capacity > m:
        raise ValueError(f"Capacity: {capacity} is greater than the number of units in the well: {m}")

    wells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                wells.append((i, j))

    # 1. preprocess the grid
    # empty wells means that there are units that can be extracted into buckets
    empty_wells = []
    for well in wells:
        if well[1] + 1 < m and grid[well[0]][well[1] + 1] > 0:
            empty_wells.append((well[0], well[1] + 1))
        if well[1] - 1 >= 0 and grid[well[0]][well[1] - 1] > 0:
            empty_wells.append((well[0], well[1] - 1))

    # 2. start from first row and check if we can empty the well
    # 3. if so, empty well by adding the contents to the bucket
    # 4. after we empty the well, move to the next row and check the same
    # process for each row.
    # 5. Once we have used all the buckets and empty the wells, we are done.
    n_buckets = math.ceil(len(empty_wells) / capacity)
    buckets = [0 for i in range(n_buckets)]
    n_extracted_units = 0
    while n_extracted_units < len(empty_wells):
        for well in empty_wells:
            if buckets
