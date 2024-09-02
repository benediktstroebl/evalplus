
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
    R, C = len(grid), len(grid[0])
    use_buckets = [[0 for _ in range(C)] for _ in range(R)]
    water_wells = [0]
    for r in range(R):
        water_wells.extend(grid[r])
    water_wells = sorted(water_wells)
    res = 0
    cap = capacity
    for w in water_wells:
        while cap > 0 and grid[R - 1][cap - 1] <= w:
            cap -= 1
        if cap == 0:
            res += 1
        else:
            use_buckets[R - 1][w - 1] += 1
    for r in range(R - 2, -1, -1):
        for c in range(C):
            use_buckets[r][c] += use_buckets[r + 1][c]
    return res
