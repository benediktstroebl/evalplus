
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

    # IDEAS:
    # 1. Brute force: Try every possible combination of buckets, record their values and
    #    return the one that gives the best result.
    # 2. Greedy: fill the grid sequentially from left to right.
    # 3. DP: build a matrix of all combinations of taking the bucket at the intersection of
    #     each row and column.
    # 4. Math: reduce the problem to finding the maximum capacity that can be filled in one pass.

    # Psuedo Code:
    # Math solution:
    # 1. reduce the problem to find the maximum capacity that can be filled in a single pass
    # 2. Get the sum of the number of 1's in a row
    # 3. Divide by the capacity to get the number of times we can fill the bucket
    # 4. Return the maximum value of the result
    # 5. Edge case: If the total capacity is less than or equal to the number of times it can fill
    #    the bucket, then return 0.

    # Base Cases
