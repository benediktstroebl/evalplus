
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
    n = len(grid)

    if not grid or not grid[0]:
        return 0

    m = len(grid[0])

    # list[list[int]]
    wells = [[0]*m for i in range(n)]

    l = list(range(m))
    r = list(reversed(range(m)))

    for row in grid:
        for i in range(m):
            if row[i] == 1:
                wells[row.index(1)][i] = 1
            else:
                wells[row.index(1)][i] = 0

    count = 0
    while l or r:
        ul = len(l)
        ur = len(r)
        if ul < ur:
            ul, r = r, l
            l, r = r, l
        elif ul == ur:
            # sometimes keeping the same row, so we don't have to
            # check all well for full capacity
            for i in range(len(l)):
                if wells[count][i] < capacity:
                    wells[count][i] += 1
            count += 1
            l = l[ur:]
            r = r[ur:]

        else:
            ul = len(l)
            ur = len(r)
            if ul > ur:
                ul, r = r, l
                l, r = r, l

            for i in range(len(l)):
                if wells[count][i] < capacity:
                    wells[count][i] += 1
                    count += 1
            l = l[ur:]
            r = r[ur:]

    return count

