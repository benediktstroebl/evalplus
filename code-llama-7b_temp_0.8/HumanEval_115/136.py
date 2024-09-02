
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
    # Naive Approach:
    # 1) Traverse the grid, filling the buckets from top to bottom
    # 2) The count is the number of rows we need to traverse

    # Optimized Approach:
    # 1) We can use the remaining water in the bucket to lower the bucket in the next row
    # 2) Let's traverse the grid in reverse order
    #    As we traverse the grid, we try to fill the bucket from the leftmost cell
    #    If the bucket is filled, we empty it at the lowest cell that is not full
    # 3) Return the count to empty the grid

    # The bucket is empty initially
    bucket_size = 0
    count = 0

    # Traverse the grid in reverse order
    for row in range(len(grid)-1, -1, -1):
        for column in range(len(grid[row])):
            # Fill the bucket
            if grid[row][column] == 1:
                bucket_size += 1
            # If the bucket is full, empty it
            if bucket_size == capacity:
                # Remove the water from the grid
                grid[row][column] -= 1
                # Decrement the bucket size
                bucket_size -= 1
                # Decrement the count
                count += 1
        # If the bucket is still full, empty it
        if bucket_size > 0:
            # Get the lowest empty cell from the next row
            next_row = row - 1
            if next_row >= 0 and next_row < len(grid) and grid[next_row][column] == 0:
                grid[next_row][column] -= 1
                # Decrement the bucket size
                bucket_size -= 1
                # Decrement the count
                count += 1
    return count
