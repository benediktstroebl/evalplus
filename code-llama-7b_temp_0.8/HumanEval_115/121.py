
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
    # we need to find the maximum sum of all the rows, while keeping the total water as 
    # low as possible
    # we can find the maximum sum of all the rows by using the capacity of the buckets
    # the sum of the rows is the total water, so we can use this to find the minimum
    # value for the sum of the rows and use that to find the total number of times we 
    # can use the buckets to fill the wells

    total_rows = len(grid)
    total_cols = len(grid[0])
    max_sum = math.inf
    for row in range(total_rows):
        current_sum = 0
        for col in range(total_cols):
            if grid[row][col] == 1:
                current_sum += 1
        if current_sum > max_sum:
            max_sum = current_sum
    
    return math.ceil(max_sum/capacity)
