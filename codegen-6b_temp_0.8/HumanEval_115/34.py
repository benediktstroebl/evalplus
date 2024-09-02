
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
    import math
    rows = len(grid)
    wells = len(grid[0])
    n_wells = wells - 1
    n_buckets = capacitiy
    buckets = [[-1 for _ in range(wells)] for _ in range(rows)]
    for r in range(rows):
        for c in range(wells):
            if grid[r][c] == 1:
                buckets[r][c] = 0
    buckets_ended = [[0 for _ in range(wells)] for _ in range(rows)]
    def _max_fill(rows, wells, n_wells, n_buckets, buckets, buckets_ended):
        if wells == 1:
            return 0
        else:
            if any(buckets_ended[r] == n_buckets and 
                    buckets[r][wells - 2] == buckets[r][wells - 1] for r in range(rows)):
                for r in range(rows):
                    if buckets[r][wells - 1] == buckets[r][wells - 2]:
                        buckets_ended[r] += 1
                return wells - 2
            else:
                # move to next well
                buckets_ended[buckets[0][wells - 1] == n_buckets - 1] += 1
                buckets_ended[buckets[0][wells - 1] == n_buckets - 2] += 1
                buckets_ended[buckets[0][wells - 1] == n_buckets - 3] += 1
                return wells - 1
    time = 0
    while True:
        time += 1
        n_wells = _max_fill(rows, wells, n_wells, n_buckets, buckets, buckets_ended)
        if n_wells == wells:
            return time
        n_buckets -= 1
        
