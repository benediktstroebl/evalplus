
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
    n, m = len(grid), len(grid[0])
    if m == 1:
        return sum(grid[0])
    elif n == 1:
        return min(m, capacity)
    else:
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = math.inf
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > capacity:
                    count += 1
                    for d in range(1, capacity + 1):
                        if i > 0 and j > 0 and grid[i - 1][j - 1] + 1 < capacity:
                            grid[i - 1][j - 1] += 1
                        if j > 0 and grid[i][j - 1] + 1 < capacity:
                            grid[i][j - 1] += 1
                        if i < n - 1 and j > 0 and grid[i + 1][j - 1] + 1 < capacity:
                            grid[i + 1][j - 1] += 1
                        if i > 0 and grid[i - 1][j] + 1 < capacity:
                            grid[i - 1][j] += 1
                        if i < n - 1 and grid[i + 1][j] + 1 < capacity:
                            grid[i + 1][j] += 1
                        if i > 0 and j < m - 1 and grid[i - 1][j + 1] + 1 < capacity:
                            grid[i - 1][j + 1] += 1
                        if j < m - 1 and grid[i][j + 1] + 1 < capacity:
                            grid[i][j + 1] += 1
                        if i < n - 1 and j < m - 1 and grid[i + 1][j + 1] + 1 < capacity:
                            grid[i +
