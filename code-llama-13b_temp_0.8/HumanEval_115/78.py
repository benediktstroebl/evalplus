
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
    # get a list with well's heights (wells at the same level should be considered as the same well)
    wells = []
    for row in grid:
        current_well = 0
        for col in row:
            if col==1:
                current_well += 1
            else:
                wells.append(current_well)
                current_well = 0
    wells.append(current_well)
    wells = list(filter(lambda x: x!=0, wells))
    
    # greedy algorithm
    bucket_loads = [0]*len(wells)
    for well in wells:
        bucket_load = 0
        for bucket in bucket_loads:
            if bucket+well<=capacity:
                bucket_load += bucket
                bucket_loads[bucket_loads.index(bucket)] = 0
            else:
                bucket_loads[bucket_loads.index(bucket)] -= capacity-well
                bucket_load += capacity-well
        bucket_loads.append(well-bucket_load)
    return sum(wells)+math.ceil(sum(bucket_loads)/capacity)
