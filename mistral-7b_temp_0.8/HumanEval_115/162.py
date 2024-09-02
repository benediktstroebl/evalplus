
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

    def greedy(grid, capacity):
        width = len(grid[0])
        height = len(grid)
        num_buckets = 0
        while True:
            rows_with_water = [i for i, row in enumerate(grid) if sum(row) > 0]
            if len(rows_with_water) == 0:
                break
            for i in rows_with_water:
                row_to_be_emptied = grid[i]
                # only continue if the current row has water
                if sum(row_to_be_emptied) > 0:
                    # extract water from the row to be emptied
                    water_extracted = min(row_to_be_emptied)
                    # remove the water from the grid
                    row_to_be_emptied = [max(0, x - water_extracted) for x in row_to_be_emptied]
                    # if the water extracted is more than the capacity of the bucket,
                    # then this row won't be able
