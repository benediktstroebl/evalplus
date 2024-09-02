
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
    well_length = len(grid[0])
    empty_wells_at_start = 0
    for row in grid:
        empty_wells_at_start += row.count(0)
    if empty_wells_at_start >= well_length:
        return 0
    
    #find the highest well first
    highest_well = 0
    for row in grid:
        highest_well = max(highest_well, row.count(1))

    # Now, if we can fill all the wells with one bucket, we don't need to do anything.
    if highest_well < well_length:
        return -1
    
    # Now, we use a loop to see how many times we have to lower the bucket
    number_of_lowered_bucket = 0
    while highest_well > 0:
        # We check how many wells can be filled using one bucket
        bucket_can_fill = math.floor(highest_well / well_length) * well_length
        # We lower the bucket to that number
        highest_well = highest_well - bucket_can_fill
        number_of_lowered_bucket += 1
        # Now, we know how many wells are filled. 
        # we check how many we can fill using the remaining bucket
        if highest_well < well_length:
            break
        else:
            # If we can fill more wells, we use the remaining bucket
            bucket_can_fill = highest_well
            highest_well = highest_well - bucket_can_fill
            number_of_lowered_bucket += 1

    return number_of_lowered_bucket

