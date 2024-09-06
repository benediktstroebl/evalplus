
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

    # first solution
    # iterate through all rows in grid, if a row has 1, that means
    # there is water in that row, and it will be removed by that row's bucket.
    # if the row is empty, skip to next row.
    # otherwise, fill bucket with water and move on to next row
    # if we have no more water left, return the current count
    # if all buckets are full, return the current count
    count = 0
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 1:
                grid[i][j] = 0
                count += 1
                if count == capacity:
                    return count

            elif value == 0 and grid[i][j-1] == 1:
                # add the amount of water in the current column to the bucket
                grid[i][j-1] = 0
                count += 1
                if count == capacity:
                    return count
    return count

    # 2
