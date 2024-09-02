
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
    # initialize the number of buckets to 1
    num_buckets = 1

    # get the row length
    row_len = len(grid[0])

    # get the number of rows
    num_rows = len(grid)

    # create a list to keep track of the number of buckets needed per row
    buckets_needed = [0] * num_rows

    # for each row
    for row in range(num_rows):
        # set the current bucket needed at zero
        buckets_needed[row] = 0

        # set the bucket count to zero
        bucket_count = 0

        # for each column
        for col in range(row_len):

            # if the current element is one
            if grid[row][col] == 1:

                # increment the bucket count
                bucket_count += 1

            # if the bucket count reaches the bucket capacity
            if bucket_count == capacity:

                # increment the number of buckets needed
                num_buckets += 1

                # set the bucket count back to zero
                bucket_count = 0

            # if the bucket count is greater than zero
            if bucket_count > 0:

                # increment the number of buckets needed in this row
                buckets_needed[row] += 1

    # return the number of buckets needed
    return num_buckets
