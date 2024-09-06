
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
    width = len(grid[0])
    length = len(grid)
    # initial state
    states = [[0 for _ in range(width)] for _ in range(length)]
    # all reachable states
    states_count = 0
    # for all reachable states (combination of filled buckets and free wells)
    # need to calculate how many times we can fill the grid
    for state in range(width**length):
        # get the bucket count for this state
        bucket_count = int(math.log2(state))
        # if the bucket count is less or equal than capacity, we can fill this state
        if bucket_count <= capacity:
            # get the bit mask of this state
            bitmask = bin(state)[2:]
            # if this state has a free well, we add it to the states count
            if bitmask[width*length - 1] == '0':
                states_count += 1
            # if this state has a filled well, we add the state count minus the bucket count
            elif bitmask[width*length - 1] ==
