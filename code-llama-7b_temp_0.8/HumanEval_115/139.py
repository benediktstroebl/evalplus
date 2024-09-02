
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

    # Add each row and see if it is over capacity.
    # If it is over capacity, then we must subtract
    # that amount from the total number of bucket
    # adjustments
    rows = len(grid)
    cols = len(grid[0])
    total_buckets = rows
    adjustments = 0
    for row in range(rows):
        current_row = grid[row]
        current_row_sum = 0
        for col in range(cols):
            current_bucket = current_row[col]
            current_row_sum += current_bucket
        total_buckets -= (current_row_sum // capacity)
        # If there are remainder in the row,
        # then we must count the number of times
        # we must lower the buckets.
        if current_row_sum % capacity != 0:
            adjustments += math.ceil(current_row_sum / capacity) - 1

    return total_buckets + adjustments
