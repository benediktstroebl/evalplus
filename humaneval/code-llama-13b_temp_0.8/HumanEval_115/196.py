
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
    bucket_level = 0
    # N = number of columns (wells)
    N = len(grid[0])
    # M = number of rows (buckets)
    M = len(grid)
    # result = number of times buckets are lowered
    result = 0
    for j in range(M):
        for i in range(N):
            # try to fill bucket
            if grid[j][i] == 1:
                bucket_level += 1
            # if bucket is full
            if bucket_level == capacity:
                result += 1
                # empty bucket
                for row in range(j, M):
                    # fill the next row
                    if grid[row][i] == 1:
                        bucket_level += 1
                    # empty the row, but be careful of negative index
                    if row+1 < M:
                        if grid[row+1][i] == 0:
                            bucket_level -= 1
                    # if bucket is full
                    if bucket_level == capacity:
                        result += 1
                        # empty bucket
                        for row in range(row, M):
                            # fill the next row
                            if grid[row][i] == 1:
                                bucket_level += 1
                            # empty the row, but be careful of negative index
                            if row+1 < M:
                                if grid[row+1][i] == 0:
                                    bucket_level -= 1
                            # if bucket is full
                            if bucket_level == capacity:
                                result += 1
                                # empty bucket
                                for row in range(row, M):
                                    # fill the next row
                                    if grid[row][i] == 1:
                                        bucket_level += 1
                                    # empty the row, but be careful of negative index
                                    if row+1 < M:
                                        if grid[row+1][i] == 0:
                                            bucket_level -= 1
                                    # if bucket is full
                                    if bucket_level == capacity:
                                        result +=
