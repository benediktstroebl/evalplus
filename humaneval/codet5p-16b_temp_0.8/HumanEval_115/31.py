
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

    def fill_bucket(grid, bucket_capacity):
        # count how many times we need to fill the bucket with water
        max_fill_count = 0
        for row in grid:
            max_fill_count += row.count(1)
        
        if max_fill_count == 0:
            return 0

        row_len = len(grid[0])
        col_len = len(grid)
        max_fill_count = math.ceil(max_fill_count / bucket_capacity)
        fill_bucket_count = 0

        # fill bucket with water
        while fill_bucket_count < max_fill_count:
            for row in grid:
                for i in range(len(row)):
                    if row[i] == 1:
                        row[i] = 0
                        fill_bucket_count += 1
                        if fill_bucket_count == max_fill_count:
                            return row_len * max_fill_count
                        else:
                            row[i] = 1

        return 0

    return fill_bucket(grid, capacity)
