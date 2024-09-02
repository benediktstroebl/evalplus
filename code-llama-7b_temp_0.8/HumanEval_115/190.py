
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
    def _max_fill(grid, capacity):
        # assuming there's only 1 bucket
        rows = len(grid)
        cols = len(grid[0])
        # create a bucket 
        bucket = 0
        times = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # add water
                    bucket += 1
                elif bucket > 0:
                    # if there's any water in the bucket, dump
                    bucket -= 1
                    times += 1

        return times

    def _max_fill_wrapper(grid, capacity, grid_h, grid_w, times, row, col):
        # assuming there's only 1 bucket
        if row == grid_h - 1:
            return times
        elif col == grid_w - 1:
            return times + _max_fill_wrapper(grid, capacity, grid_h, grid_w, 0, row + 1, 0)
        elif grid[row][col] == 1:
            # add water
            bucket = 1
            times += 1
        elif bucket > 0:
            # if there's any water in the bucket, dump
            bucket -= 1
            times += 1

        times = min(times, _max_fill_wrapper(grid, capacity, grid_h, grid_w, 0, row + 1, col + 1))
        times = min(times, _max_fill_wrapper(grid, capacity, grid_h, grid_w, bucket, row + 1, col))
        return times

    rows = len(grid)
    cols = len(grid[0])
    grid_w = math.ceil(math.sqrt(rows))
    grid_h = math.ceil(rows / grid_w)

    if rows * cols == 0:
        return 0
    
    # times = _max_fill(grid, capacity)
    # print(times)
    times = _max_fill_wrapper(grid, capacity, grid_h, grid_w, 0, 0
