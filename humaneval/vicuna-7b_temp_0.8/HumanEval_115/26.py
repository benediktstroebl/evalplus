
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
    rows,cols = grid.shape
    non_zero_cols = [i for i,val in enumerate(grid) if val != 0]
    grid_without_wells = [[0] * (cols+1) for _ in range(rows)]
    for i in non_zero_cols:
        grid_without_wells[i[0]-1][i[1]-1] = 1
    grid_without_wells = [int(val) for val in grid_without_wells]
    non_zero_cols = sorted(non_zero_cols)
    fill_buckets_count = 0
    for i in range(0,rows-1,1):
        for j in range(0,cols-1,1):
            if grid_without_wells[i][j] == 1:
                for k in range(0,int(math.ceil(capacity/1.0)))
                    if grid_without_wells[i+k][j+1] == 0:
                        grid_without_wells[i+k][j+1] = 1
                        fill_buckets_count += 1
                        if grid_without_wells[i+k][j+1] == grid[i][j]:
                            break
    return fill_buckets_count