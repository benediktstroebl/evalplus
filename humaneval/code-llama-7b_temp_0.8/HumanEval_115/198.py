
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
    if len(grid) == 1:
        return 0 if grid[0][0] == 0 else math.inf
    
    rows = len(grid)
    columns = len(grid[0])
    capacities = [0 for _ in range(len(grid))]
    result = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j]:
                capacities[i] += 1
                if capacities[i] == capacity:
                    result += 1
                elif capacities[i] > capacity:
                    return math.inf
    
    for j in range(columns):
        for i in range(rows - 1, -1, -1):
            if grid[i][j]:
                capacities[i] += 1
                if capacities[i] == capacity:
                    result += 1
                elif capacities[i] > capacity:
                    return math.inf
    
    return result
