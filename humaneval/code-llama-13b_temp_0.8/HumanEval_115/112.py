
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
    
    # Results 
    result = 0
    # Lines
    lines = len(grid)
    # Columns
    columns = len(grid[0])
    # Iterator
    it = 0
    # Cells
    cells = lines * columns
    # Capacity
    capacity = bucket_capacity
    # Spaces
    spaces = capacity * columns
    # Buckets
    buckets = cells // spaces + 1 if cells % spaces > 0 else cells // spaces
    # Explanation
    explanation = []
    # Water
    water = 0
    # Loop through buckets
    for i in range(buckets):
        # Start from top
        it = 0
        # Loop through lines
        for j in range(lines):
            # If we can get water from top
            if it + capacity <= lines:
                # Loop through columns
                for k in range(columns):
                    # Get water from top
                    water += grid[it][k]
                # Increment iterator
                it += 1
            # Else, get water from bottom
            else:
                # Get water from bottom
                water += grid[lines - 1 - (it)%lines][k]
                # Increment iterator
                it += 1
        # Add the result
        result += water
        # Add explanation
        explanation.append(water)
        # Reset water
        water = 0
    # Return result
    return result

