
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
    # print(f"grid: {grid}")

    # Total number of empty wells
    total_empty_wells = 0
    for wells in grid:
        if 0 in wells:
            total_empty_wells += 1

    # Total number of filled wells
    total_filled_wells = len(grid) * len(grid[0]) - total_empty_wells
    # print(f"total_empty_wells: {total_empty_wells}, total_filled_wells: {total_filled_wells}")

    # Total number of full buckets
    total_buckets = math.ceil(total_filled_wells / capacity)
    # print(f"total_buckets: {total_buckets}")

    # Number of empty buckets required
    empty_buckets = math.ceil(total_empty_wells / capacity)
    # print(f"empty_buckets: {empty_buckets}")

    return max(total_buckets, empty_buckets)

