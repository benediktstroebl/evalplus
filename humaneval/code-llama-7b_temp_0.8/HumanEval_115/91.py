
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
    # special cases
    if len(grid) == 0:
        return 0
    if len(grid) == 1 and len(grid[0]) == 1:
        return 0
    if capacity == 0:
        return 0
    if capacity >= len(grid[0]) * len(grid):
        return 0

    # set initial variables
    n_rows = len(grid)
    n_cols = len(grid[0])
    buckets = capacity
    n_buckets = n_rows
    cur_bucket = 0
    # moveto is a 2D array (representing a path of travel)
    moveto = []
    # complete is a boolean array. 
    # 1 means that the water has been emptied
    complete = [ [0 for _ in range(n_cols)] for _ in range(n_rows)]
    # n_complete represents the number of wells that have been emptied
    n_complete = 0

    # Auxiliary function to shift all buckets to the right
    def right_shift_buckets():
        nonlocal cur_bucket
        if cur_bucket + 1 < n_buckets:
            cur_bucket += 1
            moveto.append(cur_bucket)
            return True
        return False

    # Auxiliary function to shift all buckets to the left
    def left_shift_buckets():
        nonlocal cur_bucket
        if cur_bucket > 0:
            cur_bucket -= 1
            moveto.append(cur_bucket)
            return True
        return False

    # Auxiliary function to shift all buckets to the down
    def down_shift_buckets():
        nonlocal cur_bucket
        if (cur_bucket + 1) % n_buckets == 0:
            cur_bucket = (cur_bucket + 1) % n_buckets
            moveto.append(cur_bucket)
            return True
        return False

    # Auxiliary function to shift all buckets to the top
    def up_shift_buckets():
        nonlocal cur_bucket
        if cur_
