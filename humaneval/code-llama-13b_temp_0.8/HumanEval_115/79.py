
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
    # [1,0,1,1]
    def empty_well(well, capacity):
        # [0,0,0,0]
        bucket = [0 for _ in range(len(well))]
        times = 0
        while sum(bucket):
            times += 1
            for i in range(len(bucket)):
                if bucket[i] == 0:
                    if well[i] > 0:
                        bucket[i] = min(well[i], capacity)
                        well[i] -= capacity
                    else:
                        continue
                else:
                    if bucket[i] > well[i]:
                        bucket[i] = well[i]
                    else:
                        well[i] -= bucket[i]
                        bucket[i] = 0
        return times

    wells = [row for row in grid]
    times = 0
    while sum(map(sum, wells)) > 0:
        times += empty_well(wells[0], capacity)
        wells = list(zip(*wells[::-1]))
    return times

