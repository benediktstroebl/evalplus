
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
    min_flow = float("inf")
    sink_well = None
    while True:
        min_flow = math.inf
        for i, well in enumerate(grid):
            if grid[i][0] == 1:
                sink_well = i
                break
        if sink_well == None:
            break
        for i, row in enumerate(grid):
            if i == sink_well:
                continue
            elif row[0] == 1:
                grid[i][0] -= min(grid[i][0], min_flow)
                min_flow = 0
        grid[sink_well][0] += min_flow
    return len(grid
