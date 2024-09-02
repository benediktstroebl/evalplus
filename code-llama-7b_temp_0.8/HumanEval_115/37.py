
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

    if capacity == 0:
        return 0

    from collections import deque
    wells = []
    for i in range(len(grid)):
        wells.append(deque(grid[i]))

    def can_extract(bucket, i):
        for b in bucket:
            if not b or len(b) == 0:
                return False
            if b[-1] == 0:
                return False
        return True

    def extract(bucket, i):
        if can_extract(bucket, i):
            for b in bucket:
                if b:
                    b.pop()
    
    def fill(bucket, i):
        for b in bucket:
            if len(b) < capacity:
                b.append(i)

    def empty_all_wells(bucket, i):
        if can_extract(bucket, i):
            extract(bucket, i)
            for b in bucket:
                if len(b) < capacity:
                    b.append(i)
    
    def empty_all_buckets(bucket, i):
        if can_extract(bucket, i):
            for b in bucket:
                if len(b) < capacity:
                    b.append(i)

    if capacity == len(wells[0]):
        return 0

    if capacity >= math.sqrt(len(wells[0])):
        return len(wells) - 1

    #print(wells)

    # extract all the water from wells
    i = 1
    while i <= capacity:
        for j in range(len(wells)):
            extract(wells, i)
        i += 1
    
    #print(wells)

    # empty all the buckets
    i = 1
    while i <= capacity:
        for j in range(len(wells)):
            empty_all_buckets(wells, i)
        i += 1

    #print(wells)

    # fill all the buckets
    i = 1
    while i <= capacity:
        for j in range(len(wells)):
