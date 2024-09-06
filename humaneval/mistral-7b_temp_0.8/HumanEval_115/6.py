
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
    height = len(grid)
    width = len(grid[0])

    if height == 1 and width == 1:
        return 0

    bucket_capacity = capacity

    # count the number of water in each row
    water_counts = []
    for i in range(height):
        # sum of water in row i
        water_counts.append(grid[i].count(1))

    # number of water in a row
    min_water_count = min(water_counts)
    max_water_count = max(water_counts)
    min_waters = min_water_count * height
    max_waters = max_water_count * height

    # count the number of wells
    num_wells = 0
    for row in grid:
        num_wells += row.count(1)

    # calculate number of extra water for each bucket
    num_extra_water = max_waters - bucket_capacity * num_wells

    # number of times you need to lower the buckets
    bucket
