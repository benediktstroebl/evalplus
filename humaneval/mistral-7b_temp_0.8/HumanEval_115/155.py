
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

    # 1. Check if all the cells in the grid are 0
    # 2. Calculate the number of water units needed to fill each well
    # 3. Determine the number of times you need to lower the buckets
    # 4. Create a grid with the number of units of water needed to fill each well
    # 5. Use the min heap to find the minimum number of units of water needed to fill each well
    # 6. Use the binary heap to find the maximum number of units of water needed to fill each well

    # 1. Check if all the cells in the grid are 0
    if all([all([cell == 0 for cell in row]) for row in grid]):
        return 0

    # 2. Calculate the number of water units needed to fill each well
    unit_needed = []
    for row in grid:
        unit_needed.append([math.ceil(cell / capacity) for cell in row])

    # 3. Determine the number of times you need to lower the buckets
    num_bucket = math.ceil(max([
