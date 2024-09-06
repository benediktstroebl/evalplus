
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
    # Write your code here
    
    if len(grid) == 0:
        return 0

    # get row_length
    row_length = len(grid[0])
    # check if there is no 1
    if row_length == 0:
        return 0

    # find maximum
    max_len = max(grid, key=lambda x: sum(x))
    # get maximum
    max_amount = sum(max_len)
    # get number of buckets to fill
    no_buckets = math.ceil(max_amount / capacity)

    # count iterations
    iterations = 0
    # lower bucket
    for _ in range(no_buckets):
        for row in grid:
            if sum(row) > 0:
                iterations += 1
                # fill bucket
                for i in range(row_length):
                    if row[i] == 1:
                        row[i] = 0
                    else:
                        break
    
    return iterations


