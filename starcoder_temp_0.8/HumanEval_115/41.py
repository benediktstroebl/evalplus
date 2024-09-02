
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
    #
    # Dynamic programming
    #
    # Create a matrix that keeps track of the number of times a given well
    # needs to be lowered to empty it.
    #
    # To do this, we first initialise the first column to be 0 for every row.
    # Then, for each row, we iterate over its column. If the cell is 0,
    # we only need to increment the value on the previous cell in the row.
    # If the cell is 1, we need to increment the value on the previous cell
    # and on the previous cell's right.
    #
    # Time Complexity: O(N^2)
    # Space Complexity: O(N^2)
    #
    dp = [[0 for _ in row] for row in grid]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row == 0:
                dp[row][col] = 0
            else:
                dp[row][col] = dp[row - 1][col] + 1 if grid[row][col] == 0 else dp[row - 1][col] + 1 + dp[row - 1][col - 1]

    return len(grid) - dp[-1][-1]

