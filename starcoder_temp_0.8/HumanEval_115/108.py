
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
    R, C = len(grid), len(grid[0])

    # the lower bucket counter
    lower = 0

    # the current capacity of the bucket
    capacity = capacity

    # the last row
    row = R - 1

    # iterate from the bottom to the top row
    for r in range(R - 1, -1, -1):
        # if the first column is not zero, then we have to fill the bucket
        if grid[r][0]!= 0:
            # if the current capacity is less than the water available in that well,
            # then we have to fill the bucket
            if capacity < grid[r][0]:
                # fill the bucket
                capacity += grid[r][0] - capacity
                # increment the counter of the lower buckets
                lower += 1

            # otherwise, fill the bucket with the available water
            else:
                capacity -= grid[r][0]

        # if the last column is not zero, then we have to fill the bucket
        if grid[r][C - 1]!= 0:
            # if the current capacity is less than the water available in that well,
            # then we have to fill the bucket
            if capacity < grid[r][C - 1]:
                # fill the bucket
                capacity += grid[r][C - 1] - capacity
                # increment the counter of the lower buckets
                lower += 1

            # otherwise, fill the bucket with the available water
            else:
                capacity -= grid[r][C - 1]

        # if we reach the bottom of the row,
        # and the capacity is not full
        if r == row and capacity!= capacity:
            # fill the bucket
            capacity += capacity - capacity
            # increment the counter of the lower buckets
            lower += 1

    # return the number of lower buckets
    return lower

