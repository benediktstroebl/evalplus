
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

    # this is the maximum number of columns in the grid
    n = len(grid[0])

    # number of wells
    m = len(grid)

    # how much water can we extract
    # from the wells?
    # this will be our water capacity
    # but we need to reduce it to 
    # the amount of water we can extract
    capacity = capacity * n

    # how many times do we need to 
    # lower the bucket?
    times = 0

    for i in range(m):
        # extract the current row
        # from the grid
        row = grid[i]
        # print(row)

        # how much water do we have?
        extracted = 0

        # where in the row do we start?
        # since we can't extract water
        # from a full well
        j = 0

        # while we still have water to extract
        while extracted < capacity:
            # if we are at the end of the row
            # we're done
            if j == n:
                break
            
            # how much water can we extract?
            # if we are at the beginning of the row
            # we can extract the whole amount of water
            # otherwise we can't extract any more water
            if j == 0:
                amount = row[j]
            else:
                amount = 0

            # we can't extract any more water
            # if there are no more water units in the row
            if amount == 0:
                break

            # how much water can we extract from the well?
            can_extract = capacity - extracted

            # if we can't extract the full
            # amount of water
            if can_extract < amount:
                # we only extract the part of the well that will fit in the bucket
                amount = can_extract

            # we extract the amount of water from the well
            extracted += amount

            # we have used a bucket to extract the amount of water
            # from the well
            times += 1

            # update the amount of water in the well
            # so that we can't extract more water from it
           
