
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
    w = len(grid)
    h = len(grid[0])
    wells = grid.count(1)

    if not wells or wells == h or wells == w:
        return 0

    buckets_needed = []
    for i in range(h):
        if grid[i][0] == 1:
            buckets_needed.append(capacity)
    
    for j in range(w):
        if grid[0][j] == 1:
            buckets_needed.append(capacity)

    for k in range(1,h):
        for l in range(1,w):
            if grid[k][l] == 1:
                buckets_needed.append(capacity)
    
    import math
    print(buckets_needed)
    return int(math.ceil(wells / len(buckets_needed)))

