
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
    # Intuition:
    # Approach 1: Brute Force
    #   For each row, check the max water it can hold and 
    #       increment the count if the water fill is greater than capacity
    #   Complexity: O(mn)

    # Approach 2: Solving the problem using Dynamic Programming
    #    1. Find the maximum water that can be stored at each index of row and column of grid
    #    2. Increment the count if the maximum water at any row is greater than capacity
    #    3. Do 1 & 2 for every row

    #    4. Find the maximum water that can be stored at each index of row and column of grid
    #    5. Increment the count if the maximum water at any column is greater than capacity
    #    6. Do 4 & 5 for every column

    # 7. Return the count

    # find the max water that can be stored at each index of row and column of grid
    max_water_row = _max_water_row(grid)
    max_water_column = _max_water_column(grid)

    # increment the count if the maximum water at any row is greater than capacity
    return sum([1 for i in max_water_row if i > capacity]) + sum([1 for i in max_water_column if i > capacity])

