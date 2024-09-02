
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
    # grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # capacity : 1
    # Output: 6
    # 
    # grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    # capacity : 2
    # Output: 5
    # 
    # grid : [[0,0,0], [0,0,0]]
    # capacity : 5
    # Output: 0
    
    # Intuition:
    # For each row, find the highest water unit and its index in the row.
    # Move the bucket to that point in the row and empty it.
    # Repeat this process for all rows.
    # Update the amount of water remaining in the wells and return the max number of times we can
    # lower the bucket.
    # Keeping track of the max_amount_water helps determine the output.

    # Approach:
    # Find the highest water unit in each row.
    # Use the highest water unit in a row to determine how many times the bucket must be lowered.
    # Keep track of the max_amount_water to determine the output.

    # Edge Cases:
    # If all wells are empty, return 0.

    import math
    # grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # capacity : 1
    # Output: 6

    # grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    # capacity : 2
    # Output: 5

    # grid : [[0,0,0], [0,0,0]]
    # capacity : 5
    # Output: 0

    if grid == []:
        return 0

    # Find the max_water in each row.
    rows = len(grid)
    cols = len(grid[0])
    max
