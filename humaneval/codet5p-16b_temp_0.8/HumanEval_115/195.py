
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

    rows, columns = len(grid), len(grid[0])
    total = rows * columns
    if total == 0:
        return 0
    
    bucket_index = 1
    buckets = [capacity]
    while bucket_index <= total:
        bucket = buckets[-1]
        while bucket > 0 and bucket_index < total:
            cell = grid[bucket_index // columns][bucket_index % columns]
            if cell == 0:
                bucket -= 1
            else:
                break
        if bucket > 0:
            buckets.append(bucket)
        bucket_index += 1
    return len(buckets) - 1
    
