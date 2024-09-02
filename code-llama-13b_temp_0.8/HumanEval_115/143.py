
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
    number_of_wells = len(grid)
    number_of_columns = len(grid[0])

    # Find the longest row.
    longest_row = 0
    for row in range(number_of_wells):
        longest_row = max(longest_row, sum(grid[row]))

    # Find the maximum number of buckets that can be filled.
    number_of_buckets = int(capacity / longest_row)

    # Initialize the `buckets_filled` matrix.
    buckets_filled = [[0] * number_of_columns for _ in range(number_of_wells)]

    # Fill the buckets.
    number_of_times = 0
    for bucket in range(number_of_buckets):
        for row in range(number_of_wells - 1, -1, -1):
            if not buckets_filled[row][0]:
                number_of_times += fill_row(buckets_filled[row], grid[row])

    # Find the number of times that the buckets will have to be filled
    # in the remaining wells.
    for row in range(number_of_wells):
        if not buckets_filled[row][0]:
            number_of_times += math.ceil(sum(grid[row]) / capacity)

    return number_of_times

