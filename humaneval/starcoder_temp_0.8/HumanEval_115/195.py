
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
    # get the dimensions of the grid
    row, col = len(grid), len(grid[0])
    # now we need to find the maximum number of times we can empty the bucket
    # that way we need to fill the bucket at max capacity
    # so we can achieve that by filling each bucket till it's completely filled
    # we can achieve that by having the bucket capacity as 1
    max_count = math.ceil(capacity/col)
    # now we need to count the total number of empty times
    # we can do that by dividing total_empty_cells/capacity
    count = 0
    # first we need to find the total empty cells
    total_empty_cells = 0
    for row in grid:
        for col in row:
            if col == 0:
                total_empty_cells += 1
    # now divide total_empty_cells by capacity
    count = math.ceil(total_empty_cells/capacity)
    # return the result
    return count

