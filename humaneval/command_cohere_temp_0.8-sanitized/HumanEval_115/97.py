import math
def max_fill(grid, capacity):
    """
    Fills wells in the grid with water up to the capacity of the bucket.
    Returns the maximum number of times the bucket needs to be lowered.
    """
    if not grid:
        return 0

    # Calculate the dimensions of the grid
    row_count = len(grid)
    col_count = len(grid[0])

    # Initialize a 2D dp array to store the maximum water that can be filled
    dp = [[0 for _ in range(col_count)] for _ in range(row_count)]

    # Fill the dp array bottom-up
    for row in range(row_count):
        for col in range(col_count):
            if grid[row][col] == 1:
                for i in range(row, -1, -1):
                    if grid[i][col] == 1:
                        dp[i][col] = dp[i+1][col] + 1
                    else:
                        dp[i][col] = max(dp[i][col], dp[i+1][col])

    # Calculate the maximum number of bucket lowers