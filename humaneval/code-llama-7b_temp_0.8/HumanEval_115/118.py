
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
    # First, we find out how many "wells" we have
    row_num = len(grid)
    col_num = len(grid[0])

    # Second, we flatten the grid into a single list of "wells"
    # to make it easier to use set operations.
    well_list = [item for sublist in grid for item in sublist]

    # Third, we add a "stop" marker to the end of our list so we don't end up
    # in an infinite loop.
    well_list.append(None)

    # Fourth, we find all the starting locations of water.
    # This means finding all the locations where the value in the list is 1.
    starting_indexes = [i for i, x in enumerate(well_list) if x == 1]
    # last_starting_index = starting_indexes[-1]

    # Fifth, we loop through the starting locations and use a set to track
    # the locations of the water that we have already encountered.
    # We use a set so we can quickly check if a given location has already
    # been encountered.
    # We start by setting all locations in the grid to 0 to begin.
    grid_mod = [list(item) for item in grid]
    for x in range(0, row_num):
        for y in range(0, col_num):
            grid_mod[x][y] = 0

    # Then, we loop through the starting locations, adding water in each
    # location until the capacity is met.
    # The new location is the previous location plus the current location.
    for starting_index in starting_indexes:
        # The starting location is where we start from.
        starting_location = well_list[starting_index]
        # The current location is where we are currently at.
        # This starts at the starting location.
        current_location = well_list[starting_index]
        # The water that we have encountered is a set that we use to keep track
        # of where we have been.
        water_encountered = set()
        # The number of times we have lowered the bucket is set to
