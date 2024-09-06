
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

    if len(grid) == 0 or len(grid[0]) == 0: return 0
    total_rows = len(grid)
    total_cols = len(grid[0])
    count = 0
    for row in range(total_rows):
        for col in range(total_cols):
            if grid[row][col] == 0: continue
            curr_well_capacity = capacity
            empty_buckets = 0
            count += 1
            while grid[row][col] > 0:
                current_buckets = math.ceil(grid[row][col]/curr_well_capacity)
                empty_buckets += current_buckets
                grid[row][col] -= curr_well_capacity*current_buckets
                curr_well_capacity -= 1
            if empty_buckets > 0:
                count += empty_buckets
    return count


