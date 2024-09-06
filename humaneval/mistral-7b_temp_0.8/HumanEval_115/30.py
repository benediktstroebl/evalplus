
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
    # math.ceil() method returns the smallest integer greater than or equal to the given float.
    # math.floor() method returns the largest integer less than or equal to the given float.
    # math.log() method returns the natural logarithm of a number
    # math.sqrt() method returns the square root of a number

    # return max_fill(grid, capacity)

    # Solution 1
    # Logic:
    #       * In the first iteration, we can use the capacity to fill all the wells with the same height.
    #       * In the next iteration, we use the remaining capacity to fill all the wells with the same height.
    #       * We repeat this process until we run out of capacity.
    #       * Each iteration, we store the number of times we filled the wells with the same height.
    #       * We return the sum of all these iterations.
    # Time complexity: O(n)
    # Space complexity: O(1)
    if not grid:
        return 0

    total_wells = 0
    for row in grid:
       
