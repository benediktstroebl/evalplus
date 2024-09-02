
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
    if not grid_size: return 0
    max_fill = 0
    for i in range(grid_size):
        # if current row has empty well then continue
        if not grid[i]: continue
        # get the max_fill of the previous row
        prev_fill = max_fill
        max_fill = max(max_fill, get_max_fill(grid[i], capacity))
        # increase the previous fill by the number of times we need to go down
        # to reach the max fill for current row
        max_fill += prev_fill
        # if we need to refill bucket
        if max_fill > capacity:
            max_fill -= fill_buckets(grid[i], capacity)

    return max_fill
