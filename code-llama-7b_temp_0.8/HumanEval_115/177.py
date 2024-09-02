
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
    total_wells = 0
    for row in grid:
        for well in row:
            if well == 1:
                total_wells += 1
    # print("total wells: ", total_wells)
    filled_wells = 0
    current_bucket_capacity = 0
    current_bucket_wells = []
    result = 0
    for row in grid:
        for well in row:
            if well == 1:
                filled_wells += 1
                current_bucket_wells.append(well)
                current_bucket_capacity += well
            if well == 0:
                current_bucket_capacity += well
                filled_wells += 1
                if current_bucket_capacity == capacity:
                    # result += math.ceil(filled_wells / capacity)
                    result += 1
                elif current_bucket_capacity > capacity:
                    # result += math.ceil(filled_wells / capacity)
                    result += 1
                    while current_bucket_capacity > capacity:
                        # result += math.ceil(filled_wells / capacity)
                        result += 1
                        for well in current_bucket_wells:
                            if well == 1:
                                current_bucket_capacity -= well
                                filled_wells -= 1
                    current_bucket_wells = []
                    current_bucket_capacity = 0
                    filled_wells = 0
    return result

