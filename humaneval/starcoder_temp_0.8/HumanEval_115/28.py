
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
    # find maximum row length
    max_len = 0
    for row in grid:
        if len(row) > max_len:
            max_len = len(row)

    # can be filled with max_len
    if max_len <= capacity:
        return 0

    # count the number of 1's in each row
    counts = []
    for row in grid:
        count = 0
        for val in row:
            if val == 1:
                count += 1
        counts.append(count)

    # minimum count to fill the wells
    min_count = min(counts)
    if min_count == 0:
        return 0

    # fill the wells
    count = 0
    for i in range(len(counts)):
        if counts[i] == 0:
            continue
        else:
            buckets = math.ceil(counts[i] / capacity)
            count += buckets
    return count
