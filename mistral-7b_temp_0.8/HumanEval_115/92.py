
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

    ## Your Code Here ##
    ## You should not modify any existing code ##

    # initialize best so far to max value of capacity
    best = capacity

    # loop through each row of grid
    for row in range(len(grid)):

        # initialize count and capacity to zero
        count = 0
        capacity = 0

        # loop through each column of the row
        for column in range(len(grid[row])):

            # if column has water
            if grid[row][column] == 1:

                # add capacity to current capacity
                capacity += 1

                # if capacity is greater than or equal to capacity
                if capacity >= capacity:

                    # if current count is less than best
                    if count < best:

                        # set best to current count
                        best = count

                    # reset capacity to zero
                    capacity = 0

                    # reset count to current count plus one
                    count += 1

    # return best
    return best

    # Time: O(n)
