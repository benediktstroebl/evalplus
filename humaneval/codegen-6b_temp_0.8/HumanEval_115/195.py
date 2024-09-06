
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
    num_row = len(grid)
    num_col = len(grid[0])
    "Build height list"
    height_list = []
    for row in grid:
        height_list.append(sum(row))

    current_height = max(height_list)
    num_bucket = math.ceil(current_height / capacity)
    
    while num_row > 1:

        for i in range(num_col):
            if grid[num_row - 1][i] == 1:
                current_height -= height_list[num_row - 1]
                grid[num_row - 1][i] = 0

        if current_height <= 0:
            break
        
        if max(height_list) <= current_height:
            current_height = max(height_list)
            num_bucket += 1

        num_row -= 1
        height_list = height_list[:-1]
        for row in grid:
            height_list.append(sum(row))

    return num_bucket

