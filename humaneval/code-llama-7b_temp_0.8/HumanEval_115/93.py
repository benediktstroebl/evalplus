
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

    # A: count the wells with water
    num_wells = sum([sum(1 for x in row if x == 1) for row in grid])
    
    # B: count the buckets
    num_buckets = len(grid[0])

    # C: count how many times to lower the buckets
    num_lower = math.ceil(num_wells / num_buckets)

    # D: calculate the number of water extracted in each round
    num_water_per_round = capacity * num_buckets
    
    # E: calculate the number of times the water needs to be lowered
    while num_water_per_round > num_wells:
        # reset the num_water_per_round and lower one round
        num_water_per_round = num_buckets * (capacity - 1)
        num_lower += 1

    return num_lower

