
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
    # we only have to use the buckets to lower the wells
    # so we need to know how many times to raise the buckets
    # we know that there is only 1 well in each row, so we can simply sum the rows
    # if we exceed capacity, we need to lower the buckets by 1
    # if we are below capacity, we need to raise the buckets by 1
    def sum_rows(grid):
        total = 0
        for row in grid:
            total += sum(row)
        return total

    def max_rows(grid):
        total = 0
        for row in grid:
            total += math.ceil(sum(row) / bucket_capacity)
        return total

    def max_columns(grid):
        total = 0
        for col in range(len(grid[0])):
            total += math.ceil(sum([row[col] for row in grid]) / bucket_capacity)
        return total
    
    def max_wells(grid):
        return max(sum_rows(grid), max_columns(grid), max_rows(grid))

    bucket_count = 1
    while max_wells(grid) > capacity:
        bucket_count += 1

    return bucket_count

