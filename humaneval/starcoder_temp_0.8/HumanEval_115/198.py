
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
    m = len(grid[0])

    # get available buckets
    available = list()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                available.append((i, j))

    # sort available buckets
    available.sort(key=lambda item: item[0] * m + item[1])

    # use buckets
    num_buckets = 0
    while len(available):
        # get bucket
        item = available.pop()
        i, j = item[0], item[1]
        grid[i][j] = 0

        # check neighbors
        for x, y in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
            if x < 0 or x >= n or y < 0 or y >= m:
                continue

            if grid[x][y] == 1:
                available.append((x, y))

        num_buckets += 1

    return num_buckets

