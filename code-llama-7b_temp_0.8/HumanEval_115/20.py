
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
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def min_bucket_needed(row, col):
        if row == rows:
            return 0
        if grid[row][col] == 0:
            return 0
        if col == cols:
            return math.inf
        if row == rows:
            return math.inf
        if grid[row][col] == 0:
            return math.inf

        return min(min_bucket_needed(row, col+1), min_bucket_needed(row+1, col)) + 1

    @lru_cache(maxsize=None)
    def max_well_filled(row, col):
        if row == rows:
            return 0
        if grid[row][col] == 0:
            return 0
        if col == cols:
            return math.inf
        if row == rows:
            return math.inf
        if grid[row][col] == 0:
            return math.inf

        return max(max_well_filled(row, col+1), max_well_filled(row+1, col)) + 1

    max_count = 0

    for row in range(rows):
        for col in range(cols):
            if min_bucket_needed(row, col) <= capacity:
                max_count += max_well_filled(row, col)

    return max_count

