
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
    n = len(grid)
    m = len(grid[0])
    # we can't use a capacity bigger than the biggest well
    if m > capacity:
        capacity = m
    # we can't fill the wells if the biggest well is bigger than the capacity
    if m > capacity:
        return 0
    # we can't fill the wells if the number of rows is bigger than the capacity
    if n > capacity:
        return 0

    # if all the wells are empty, we return 0
    if not any(grid):
        return 0

    # first find all the wells that are not empty and sort them based on capacity
    # wells is a tuple with the index of the well and its capacity
    wells = sorted([(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1], key=lambda x: x[1])
    # we start from the well with the least capacity
    current_well = wells[0][0]
    current_capacity = wells[0][1]
    # the first well is full
    grid[current_well][0] = 0
    # the bucket is empty
    bucket = 0
    # the number of times we fill the bucket
    times_fell = 0

    while current_well != n:
        bucket += 1
        # if the bucket is full, we empty it
        if bucket == capacity:
            bucket = 0
            times_fell += 1
        # we try to fill the well
        try:
            # if the well is full, we go to the next one
            if grid[current_well][current_capacity - bucket] == 0:
                current_well += 1
                current_capacity = wells[current_well][1]
            # if the well is not full, we fill it
            else:
                grid[current_well][current_capacity - bucket] = 0
        # if the well doesn't exist, we start from the beginning
        except:
            times_fell += 1
            current_well = 0
            current_
