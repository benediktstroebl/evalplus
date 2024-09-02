
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

    bucket_capacity = capacity
    well_length = len(grid[0])
    well_width = len(grid)
    well_total = well_length * well_width
    bucket_total = bucket_capacity * well_total

    def fill_wells(well_total, bucket_total, well_length, well_width, grid):
        '''
        How to fill wells?
        - Start with well 0
        - Fill bucket with capacity
        - Increment bucket
        - If bucket full, increment well
        - Repeat until all buckets filled
        '''
        bucket_count = 0
        well_count = 0
        well_id = 0

        while well_count < well_total:
            if grid[well_count // well_width][well_count % well_length] == 1:
                bucket_count += 1
                if bucket_count == bucket_total:
                    return well_count
                grid[well_count // well_width][well_count % well_length] = 0
                grid[well_id // well_width][well_id % well_
