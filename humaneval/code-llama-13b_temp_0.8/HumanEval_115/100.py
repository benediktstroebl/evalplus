
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
    def _move_to_empty_well(i, j):
        # move to the left
        for k in range(j, 0, -1):
            if grid[i][k-1] == 0:
                grid[i][k-1] = 1
                grid[i][k] = 0
                return k-1, k
        # move to the right
        for k in range(j, len(grid[i])):
            if grid[i][k+1] == 0:
                grid[i][k+1] = 1
                grid[i][k] = 0
                return k+1, k

        # move to the top
        for k in range(i, 0, -1):
            if grid[k-1][j] == 0:
                grid[k-1][j] = 1
                grid[k][j] = 0
                return k, k-1
        # move to the bottom
        for k in range(i, len(grid)):
            if grid[k+1][j] == 0:
                grid[k+1][j] = 1
                grid[k][j] = 0
                return k, k+1

    # print("first grid")
    # for row in grid:
    #     print(row)
    n_wells = len(grid)
    m_wells = len(grid[0])

    # create a queue of empty wells, (i, j)
    empty_wells = []
    for i in range(n_wells):
        for j in range(m_wells):
            if grid[i][j] == 0:
                empty_wells.append((i, j))
    n_empties = len(empty_wells)

    # fill all wells
    n_fills = 0
    while n_empties > 0:
        # find a well to fill
        i, j = empty_wells.pop(0)
        # print(i, j)

        # find a well to empty
        k, l = _move_to_empty_well
