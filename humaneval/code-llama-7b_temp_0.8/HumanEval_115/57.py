
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
    if not grid:
        return 0
    
    height, width = len(grid), len(grid[0])
    result = 0
    buckets = [0] * len(grid)

    for i in range(height):
        for j in range(width):
            if grid[i][j]:
                buckets[i] += 1
    
    while any(buckets):
        result += 1
        n_buckets = len(buckets)
        for i in range(n_buckets):
            if buckets[i]:
                current = min(buckets[i], capacity)
                buckets[i] -= current
                if i == n_buckets - 1:
                    continue
                for j in range(i + 1, n_buckets):
                    buckets[j] += current
                    current = 0

    return result

