
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
    # # Submitting this code will result in a Time Limit Exceeded.
    # # It is not the most efficient way to solve the problem.
    # # Look at max_fill_efficient for a more efficient solution.
    # # 
    # # A simple way to solve this problem is to iterate over each row,
    # # and for each row iterate over each column. 
    # # The problem is that there are up to O(N*M) rows and columns to consider.
    # #
    # # Consider, in the first example, the top row, which is filled with water.
    # # We know that if we start filling the top row, we can fill all of the 1s.
    # # But if we start filling the 2nd row, we will fill the water in the 2nd column,
    # # but we will not be able to fill the water in the first column.
    # # If we start filling the 3rd row, we will fill the water in the 3rd column,
    # # and we will not be able to fill the water in either the 2nd or 3rd columns.
    # #
    # # Therefore, we need to consider each row, and for each row consider the 
    # # longest stretch of water on that row, and how far back it is.
    # #
    # # Let's look at the first row, and call the first column in that row "column 0."
    # # We know that the water in that row cannot be filled until column 0.
    # # The reason for this is that the water in that row will only flow to the right.
    # # Similarly, we can consider the second column, and call it "column 1."
    # # We know that the water in that row cannot be filled until column 1.
    # # The reason for this is that the water in that row will only flow to the right.
    # #
    # # However, what about the 3rd column? We know that the water in that row cannot
    # # be filled until column 1. Why? Because the water can flow all the way to the right,
    # # but only to the right. That means that if we fill column 1, then
