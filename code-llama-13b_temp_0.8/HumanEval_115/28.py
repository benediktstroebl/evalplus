
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
    # return 0 if no water exists
    if sum(sum(x) for x in grid) == 0:
        return 0
    # initialize max_buckets
    max_buckets = capacity
    # initialize initial_height
    initial_height = max_buckets
    # while initial_height is greater than zero
    while initial_height > 0:
        # initialize total_buckets
        total_buckets = 0
        # iterate through grid
        for i in range(len(grid)):
            # get the max number of buckets available
            # to the current grid row
            max_buckets_for_row = math.ceil(
                sum(grid[i][:initial_height]) / initial_height)
            # if the max number of buckets for the row is less than the max buckets
            if max_buckets_for_row < max_buckets:
                # set the max buckets equal to the max number of buckets for the row
                max_buckets = max_buckets_for_row
            # if the max number of buckets for the row is equal to the max buckets
            if max_buckets == max_buckets_for_row:
                # set the total_buckets to the sum of the row
                total_buckets += sum(grid[i][:initial_height])
        # if the total_buckets is less than the number of water
        if total_buckets < sum(sum(x) for x in grid):
            # increment the initial height
            initial_height += 1
        # otherwise, return the initial height
        else:
            return initial_height
    # return the initial height
    return initial_height

