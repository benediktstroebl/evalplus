
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
    if grid == [] or len(grid) == 0 or grid[0] == []:
        return 0
    N = len(grid)
    M = len(grid[0])

    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    count = 0
    while True:
        flag = False
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    for d in directions:
                        row = i + d[0]
                        col = j + d[1]
                        if row >= 0 and row < N and col >= 0 and col < M:
                            if grid[row][col] == 1:
                                grid[i][j] = 0
                                flag = True
                                break
                        else:
                            continue
                    if flag:
                        break
        if flag:
            count += 1
        else:
            break
    return count

