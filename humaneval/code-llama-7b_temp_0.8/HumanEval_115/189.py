
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
    # initialization & pre-processing
    capacity = int(capacity)
    wells = len(grid[0])
    buckets = len(grid)
    # print(f"wells: {wells}, buckets: {buckets}, capacity: {capacity}")

    # solving the problem
    current_water = 0
    times = 0
    while current_water < wells:
        current_water = 0
        times += 1
        for i in range(buckets):
            # print(f"{i}-> {grid[i]}")
            current_water += sum(grid[i])
            if current_water < wells:
                # print(f"current_water < wells")
                possible_extract_water = min(
                    sum(grid[i]), capacity - sum(grid[i]))
                current_water += possible_extract_water
                grid[i] = [1 if x >= possible_extract_water else 0 for x in grid[i]]
                # print(f"possible_extract_water: {possible_extract_water}, current_water: {current_water}")
                # print(f"{i}->{grid[i]}")
            else:
                # print(f"current_water >= wells")
                current_water -= sum(grid[i])

    return times
