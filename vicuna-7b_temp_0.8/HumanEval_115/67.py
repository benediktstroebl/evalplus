
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
    n = grid.length
    m = grid[0].length
    empty = [0] * n
    full = [0] * n
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                empty[i] = j
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            if full[i] >= capacity:
                return full[i]
            for k in range(full[i]):
                if grid[full[i]-k][empty[i]] == 0:
                    continue
                if max(grid[full[i]-k+1][empty[i]],grid[full[i]-k+2][empty[i]]) < capacity:
                    return full[i]
                if grid[full[i]-k][empty[i]] > capacity:
                    full[i] = full[i] - k
                break
    return full[i]