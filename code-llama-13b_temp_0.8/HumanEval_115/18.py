
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
    # maps a given row to the sum of its values
    sums = [sum(row) for row in grid]
    # get the index of the row with the maximum amount of water
    # this is the row we'll take water from
    start = sums.index(max(sums))
    # keep track of the number of water we can take from the current row
    amount = 0
    # keep track of the number of times we lower the bucket
    count = 0
    # for every row in our grid
    for i in range(len(grid)):
        # if we've reached the end, we're done
        if i == len(grid) - 1:
            break
        # otherwise, we update the number of water we can take from the current row
        amount = sums[i]
        # we start at the next row and go until the end
        for j in range(i + 1, len(grid)):
            # we update the amount of water we can take
            # if the amount is greater than the capacity of the bucket, we're done
            amount += sums[j]
            # if we don't have enough water to fill the bucket, we're done
            if amount < capacity:
                break
            # otherwise, we can fill the bucket
            count += 1
            # we don't have to take any water from this row
            amount = 0
        # if we have more water than the capacity of the bucket, we can't fill the bucket
        if amount > capacity:
            break
        # otherwise, we can fill the bucket
        count += 1
    # we're done
    return count
