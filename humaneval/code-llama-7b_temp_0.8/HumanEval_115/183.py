
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
    # Initialize variables
    wells = []
    buckets = []

    # Calculate the number of buckets required
    for row in grid:
        for value in row:
            if value == 1:
                wells.append(value)
                buckets.append(0)

    # Create a list of the number of filled wells in each row
    filled_wells = []
    for row in grid:
        count = 0
        for value in row:
            if value == 1:
                count += 1
        filled_wells.append(count)
    
    # Calculate the number of bucket needed
    bucket_count = math.ceil(sum(filled_wells)/capacity)
    print(f"Buckets needed: {bucket_count}")

    # Populate the buckets with the water
    for i in range(bucket_count):
        for well in wells:
            if well == 1:
                buckets[wells.index(well)] += 1
    
    # Place the water into the wells
    for i in range(len(buckets)):
        if buckets[i] > 0:
            buckets[i] -= 1
            wells[i] = 0

    # Return the number of times the buckets have been lowered
    if sum(filled_wells) == 0:
        return 0
    return sum(buckets)/sum(filled_wells)
