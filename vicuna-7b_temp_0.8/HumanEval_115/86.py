
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
    if grid.length == 0 or grid.length == 1 or grid.length == grid[0].length:
        return 0
    if grid.length == 2:
        return 1

    for i in range(grid.length):
        for j in range(grid[0].length):
            if grid[i][j] == 1:
                bucket_index = grid.index(i, j)
                if bucket_index.row + bucket_index.col - 1 in grid:
                    num_of_1 = grid[bucket_index.row + bucket_index.col - 1][0]
                    if num_of_1 == 1:
                        return grid.index(i, j).row + 1
                    elif num_of_1 >= capacity:
                        return grid.index(i, j).row + 2
                    else:
                        return grid.index(i, j).row + 1
    return grid.length + 1