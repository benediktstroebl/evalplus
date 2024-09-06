
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
    # Return
    num_of_wells = len(grid)
    max_fill_per_well = capacity * num_of_wells
    max_fill_per_row = num_of_wells * capacity
    min_num_of_fills = math.ceil(max_fill_per_row / max_fill_per_well)

    # Edge case
    if min_num_of_fills == 0:
        return 0
    
    # Fill wells
    num_of_fills = min_num_of_fills
    for row_num in range(num_of_wells):
        row = grid[row_num]
        num_of_empty_wells = row.count(0)
        if num_of_empty_wells == 0:
            continue

        # Fill empty wells
        for empty_well_num in range(num_of_empty_wells):
            # Check if bucket capacity is enough
            if num_of_fills >= max_fill_per_well:
                num_of_fills = max_fill_per_well
                break

            # Check if row capacity is enough
            num_of_buckets = row.count(1)
            if num_of_buckets <= num_of_fills:
                num_of_fills = num_of_buckets
                break

        # Fill buckets
        num_of_buckets = row.count(1)
        if num_of_fills >= num_of_buckets:
            num_of_buckets_to_fill = num_of_buckets
        else:
            num_of_buckets_to_fill = num_of_fills
        row_buckets = row.count(1)
        for bucket_num in range(num_of_buckets_to_fill):
            row[row_buckets-bucket_num-1] = 0

        # Update number of fills
        num_of_fills -= num_of_buckets_to_fill

    return num_of_fills
