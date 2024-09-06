
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
    # Remove the comment below before submitting
    # if __name__ != '__main__':
    #     return
    """
    * 1 <= grid.length <= 10^2
    * 1 <= grid[:,1].length <= 10^2
    * grid[i][j] -> 0 | 1
    """
    num_rows = len(grid)
    num_cols = len(grid[0])
    # for every row
    for i in range(num_rows):
        # if it's empty
        if grid[i] == [0]*num_cols:
            # continue
            continue
        # find the first 1
        j = 0
        while grid[i][j] == 0:
            j += 1
        # while bucket can hold
        while j < num_cols and grid[i][j] == 1:
            # fill with bucket
            grid[i][j] = capacity
            # check the wells above and below
            if i > 0:
                grid[i-1][j] = min(grid[i-1][j], capacity)
            if i < num_rows - 1:
                grid[i+1][j] = min(grid[i+1][j], capacity)
            # increase the bucket capacity
            capacity += 1
            # continue
            j += 1
    return math.prod(grid[i])

