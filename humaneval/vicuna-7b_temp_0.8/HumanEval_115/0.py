
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

    #
    # 1. Using a queue to keep track of the wells to be emptied
    #
    q = [(0, grid[0][0])]
    while q:
        #
        # 2. Pop the well with the most water from the queue
        #
        (i, j) = q.pop()
        bucket = j
        while j < len(grid) and grid[j][0] == 1:
            j += 1
        #
        # 3. If the well is completely filled, go to the next row
        #
        if j == len(grid):
            i += 1
            j = 0
            while i < len(grid) and grid[i][0] == 1:
                i += 1
            #
        # 4. If the bucket is full, go to the next bucket
        #
        if bucket == bucket_capacity - 1:
            bucket = 0
        #
        # 5. Drain the bucket
        #
        grid[i][j] = 0
        bucket += 1
        #
        # 6. Fill the bucket
        #
        if bucket_capacity - bucket >= 1:
            grid[i][j] = 1
        q.append((i, j))
