
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

    # initialize the left and right pointer to the start of the grid
    left = 0
    right = len(grid[0]) - 1

    # max number of operations to empty the grid
    operations = 0
    while left < len(grid):
        if grid[left][right] == 0:
            left += 1
        else:
            # we have reached a filled well, so we can empty it
            # we need to add the total number of operations to the current row and column
            operations += (right - left) + 1
            # we will try to empty the current row by filling up the buckets
            # from the left until we hit a 0, or the bucket capacity
            while left < len(grid) and grid[left][right] == 1:
                # fill up the bucket from the left until we hit a 0, or the bucket capacity
                for i in range(left, len(grid)):
                    if grid[i][right] == 1:
                        grid[i][right] = 0
                        break
                # we have now filled up the buckets on this row, move left to the next
                left += 1
            # we will try to empty the current column by filling up the buckets
            # from the right until we hit a 0, or the bucket capacity
            while left < len(grid) and grid[left][right] == 0:
                # fill up the bucket from the right until we hit a 0, or the bucket capacity
                for i in range(right, -1, -1):
                    if grid[left][i] == 1:
                        grid[left][i] = 0
                        break
                # we have now filled up the buckets on this column, move right to the next
                right -= 1
    return operations

