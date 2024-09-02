
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

    if not grid or not grid[0]:
        return 0

    # Calculate the number of buckets needed to empty the wells
    number_buckets_needed = math.ceil(
        sum([sum(i) for i in grid]) / capacity)

    # Loop through the rows of the wells and count the number of times the bucket will pass over the
    # wells
    wells_visited = 0
    for row in grid:
        if sum(row) == 0:
            continue

        index = row.index(1)
        row_length = len(row)

        # Number of times the bucket will pass over the wells
        row_visited = math.ceil((row_length - index) / capacity)
        wells_visited += row_visited

    return number_buckets_needed - wells_visited

