
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
    # Try to solve the problem inplace
    # Here are the key points of the approach:
    # * Iterate in all the grid by columns, from right to left
    # * The first iteration can be done in O(n) time 
    # * The next iterations can be done in O(m) time
    # * The last iteration is a simple iteration
    # * In the case of the first iteration, the value of the maximum element is known
    # * In the case of the other iterations, the value of the maximum element is not known.
    # * To find the max, we use the algorithm proposed here:
    #     https://stackoverflow.com/questions/47963392/how-to-find-the-maximum-value-from-a-row-of-a-matrix-in-on-time-and-o1-space
    # * The same algorithm can be used to find the max value in the previous rows
    # * Once the max value is known, we can calculate the number of times that the bucket must be lowered
    # * Finally, we just need to know how many times we can fill the bucket from the first row
    # * Finally, we just need to know how many times we can fill the bucket from the first row
    #
    # NOTE: The number of times that we need to lower the bucket can be reduced in the following cases:
    # * There are no water in the last row -> just fill the bucket
    # * The max value is bigger than the bucket capacity
    # * The total number of water is smaller than the bucket capacity
    # * If there is more water than the bucket capacity and there is at least a zero value
    #   in the previous row, we can stop the iteration

    if not grid:
        return 0

    # Number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # The number of times that we need to lower the bucket
    result = 0

    # The number of times that we need to fill the bucket
    bucket_full = 0

    # The number of water in the last row
    total_water = 0

    # The max value of the last row
    
