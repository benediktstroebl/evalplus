
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

    # ============ Get input ============
    grid = [[int(char) for char in row.strip()] for row in grid.strip().split()]
    capacity = int(capacity)
    # ============ Get input ============

    m = len(grid)
    n = len(grid[0])

    # ============ Initialize ============
    # Add source as an empty well.
    grid.insert(0, [0] * n)
    grid.append([0] * n)
    for _ in range(capacity):
        grid.insert(0, [0] * n)
        grid.append([0] * n)
    # ============ Initialize ============

    # ============ Calculate ============
    # Find the maximum flow from one well to the next.
    # We use the maximum flow algorithm to calculate the maximum flow.
    # Using a queue to simulate a BFS, we can calculate the maximum flow.
    # If there is a path from the source to the sink, then the maximum flow is the amount of water that can be transported along that
