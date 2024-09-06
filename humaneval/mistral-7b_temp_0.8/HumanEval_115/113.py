
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
    # corner cases
    if grid is None or grid == []:
        return 0
    row, col = len(grid), len(grid[0])
    # if capacity is greater than the number of units of water in the wells
    # then return 0
    if capacity >= sum([sum(row) for row in grid]):
        return 0
    # initialize a 2D grid to keep track of the number of times we need to lower the bucket
    # to empty each well
    grid2 = [[math.inf for i in range(col)] for i in range(row)]
    # initialize a list of visited cells
    visited = []
    # initialize the source well
    source_row, source_col = 0, 0
    # set the number of times we need to lower the bucket to empty the source well to 0
    grid2[source_row][source_col] = 0
    # initialize the queue
    queue = [(source_row, source_col)]
    # iterate until the queue is empty
    while queue:
        # dequeue the current cell
        cur
