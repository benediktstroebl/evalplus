
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
    wells = []
    for i in range(len(grid)):
        wells.append(grid[i][0:len(grid[i])])
    
    b = {}
    for i in wells:
        b[i] = 0

    h = {}
    for i in wells:
        h[i] = len(i) - 1
    
    buckets = [0 for _ in range(len(wells))]
    
    i = 0
    while True:
        if buckets == [cap for cap in buckets]:
            return buckets
        
        curr = wells[i]
        capacity = buckets[i]
        #print(curr,capacity)
        if capacity == h[curr]:
            for j in range(len(curr)):
                if buckets[i] < capacity:
                    buckets[i] += 1
                    if curr[j] == 1:
                        buckets[wells.index(curr)] -= 1
            i += 1
        else:
            for j in range(len(curr)):
                if buckets[i] < capacity:
                    buckets[i] += 1
                    if curr[j] == 1:
                        buckets[wells.index(curr)] -= 1
            h[curr] -= 1
            if buckets[i] == h[curr]:
                i += 1
    return buckets
