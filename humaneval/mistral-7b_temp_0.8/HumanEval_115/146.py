
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
    # TODO: Your code here

    if len(grid) == 0:
        return 0

    bucket_count = 0
    # check each row of the grid
    for row in grid:
        # calculate the remaining capacity of the bucket
        remain_cap = capacity
        # iterate over each element in the row
        for i in range(len(row)):
            # if the current element is 1,
            if row[i] == 1:
                # decrease the remaining capacity by 1
                remain_cap -= 1
                # if the remaining capacity is zero,
                if remain_cap == 0:
                    # increment the bucket count by 1
                    bucket_count += 1
                    # reset the remaining capacity to the capacity of the bucket
                    remain_cap = capacity
        # if there are elements remaining in the row and the bucket is not full,
        if remain_cap > 0:
            # increment the bucket count by the number of remaining elements
            bucket_count += remain_cap

    return bucket_count




