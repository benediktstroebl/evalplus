
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
    def left(i, j):
        return j - 1
    
    def right(i, j):
        return j + 1
    
    def up(i, j):
        return i - 1
    
    def down(i, j):
        return i + 1

    def is_safe_left(i, j):
        return 0 <= j - 1 < m

    def is_safe_right(i, j):
        return 0 <= j + 1 < m

    def is_safe_up(i, j):
        return 0 <= i - 1 < n

    def is_safe_down(i, j):
        return 0 <= i + 1 < n
    
    # Traverse the grid
    def count_buckets_empty(grid, bucket_capacity):
        nonlocal n, m
        buckets = []
        empty_wells = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    empty_wells += 1
                    buckets.append((i, j))
        return empty_wells, buckets, bucket_capacity

    # Traverse the grid
    def fill_wells(grid, bucket_capacity):
        nonlocal n, m
        empty_wells, buckets, capacity = count_buckets_empty(grid, bucket_capacity)
        while empty_wells:
            for well in buckets:
                if well:
                    # Extract water from the well
                    # If the well is full, move on to the next well
                    if grid[well[0], well[1]] >= capacity:
                        continue
                    # check the adjacent wells
                    for i, j in [left(well[0], well[1]), right(well[0], well[1]), up(well[0], well[1]), down(well[0], well[1])]:
                        if is_safe_left(well[0], well[1]):
                
