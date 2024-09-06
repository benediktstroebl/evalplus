
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

    import copy
    def fill_bucket(grid, bucket_capacity, current_bucket):
        nonlocal bucket_count
        curr_well = len(grid[0])
        for row in grid:
            if 1 in row:
                next_well = row.index(1)
                if next_well!= curr_well:
                    current_bucket += grid[curr_well][next_well]
                    grid[curr_well][next_well] = 0
                    grid[next_well][curr_well] = 0
                current_bucket += grid[curr_well][next_well]
                grid[curr_well][next_well] = 0
                grid[next_well][curr_well] = 0
            curr_well = next_well
        if current_bucket < bucket_capacity:
            bucket_count += 1
        return grid, current_bucket

    bucket_count = 0
    grid = copy.deepcopy(grid)
    bucket_capacity = capacity
    current_bucket = 0
    while True:
