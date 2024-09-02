
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

    def is_empty(well):
        return math.floor(well / capacity) == 0

    def is_full(well):
        return math.floor(well / capacity) == 1

    def is_full_row(row):
        return sum([1 if is_full(w) else 0 for w in row]) == len(row)

    def is_full_col(col):
        return sum([1 if is_full(w) else 0 for w in col]) == len(col)

    def fill_wells(grid, capacity):
        count = 0
        for row in grid:
            if is_full_row(row):
                continue
            for well in row:
                if is_empty(well):
                    well += capacity
                    count += 1
        return count

    def lower_buckets(grid, capacity):
        count = 0
        for row in grid:
            for well in row:
                if is_full(well):
                    well -= capacity
                    count += 1
        return count

    def lower_buckets_col(grid, capacity):
        count = 0
