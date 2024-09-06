
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
    # 1. create a 2d array to represent the grid
    # 2. calculate the number of empty wells
    # 3. for each empty well, fill it with capacity water
    # 4. count the number of full wells
    # 5. return the number of times you need to lower the buckets
    # 6.


    n = len(grid)
    m = len(grid[0])
    num_empty_wells = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                num_empty_wells += 1
    return num_empty_wells * capacity

    # 7.


    # 8.

    # 9.

    # 10.

    # 11.
