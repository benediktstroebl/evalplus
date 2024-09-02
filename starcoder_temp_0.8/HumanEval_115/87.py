
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

    # 1st approach
    # O(n^2 * w) time | O(n^2) space
    # n -> num rows
    # w -> num cols
    # n^2 -> number of wells
    # worst case: one well and all water falls in it
    # O(n^2 * w) time | O(n^2) space
    # O(n^2 * w) time | O(n^2) space

    if not grid:
        return 0

    # we're going to store the min_levels of each well in a 2d list
    min_levels = []
    # we're going to store the filled levels of each well in a 2d list
    filled_levels = []

    num_rows = len(grid)
    num_cols = len(grid[0])

    # get the min level for each well
    for row in range(num_rows):
        row_levels = []
        row_filled_levels = []

        for col in range(num_cols):
            if grid[row][col] == 1:
                row_levels.append(math.inf)
                row_filled_levels.append(0)
            else:
                row_levels.append(row)
                row_filled_levels.append(1)

        min_levels.append(row_levels)
        filled_levels.append(row_filled_levels)

    # do BFS to get min levels
    for row in range(num_rows):
        for col in range(num_cols):
            min_level = min_levels[row][col]

            # if we can get a min level from a neighbor
            # the min level is the min of that and the current row
            if row - 1 >= 0 and filled_levels[row - 1][col] == 1:
                min_level = min(min_level, min_levels[row - 1][col] + 1)

            if row + 1 < num_rows and filled_levels[row + 1][col] == 1:
                min_level = min(min_level, min_levels[row + 1][col] + 1)

            if col - 1 >= 0 and filled_levels[row][col - 1] == 1:
                min_level = min(min_level, min_levels
