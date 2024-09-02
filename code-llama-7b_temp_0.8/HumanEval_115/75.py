
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

    # Return 0 if grid is empty
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    # Compute the number of columns
    num_columns = len(grid[0])

    # Create a bucket (i.e., list) to store the accumulated sum of rows
    bucket = [0 for _ in range(num_columns)]

    # Start from the bottom-right
    max_row = len(grid) - 1
    min_col = 0
    max_col = num_columns - 1

    # Initialize a count to store the number of times buckets are lowered
    count = 0

    # while all the wells are not empty
    while max_row >= 0 and max_col >= min_col:
        # Loop over all columns in the current row
        for col in range(min_col, max_col + 1):
            # Increment the bucket value
            bucket[col] += grid[max_row][col]
        
        # While the current bucket is larger than the capacity
        while bucket[min_col] >= capacity:
            # Decrement the bucket value
            bucket[min_col] -= capacity
            # Increment the count
            count += 1
        # Move to the next column
        min_col += 1
        # Move to the next row
        max_row -= 1
    
    return count
