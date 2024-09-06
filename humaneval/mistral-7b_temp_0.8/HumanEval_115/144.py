
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
    #get the length of each row and column
    row_length = len(grid)
    col_length = len(grid[0])
    #get the number of water units in each well
    n = 0
    for row in grid:
        n += row.count(1)

    #check if we have enough buckets
    if n >= capacity:
        return 0
    #get the number of buckets we need
    required_buckets = math.ceil(n/capacity)
    #get the number of times we have to fill our buckets
    required_times = required_buckets*row_length*col_length
    #check if we have enough buckets
    if required_times >= capacity:
        return required_times
    return required_times

