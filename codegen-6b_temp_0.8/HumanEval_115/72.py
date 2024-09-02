
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
    # row = list(enumerate(itertools.chain(*grid)))
    # print(row)
    # maxdonate = 0
    # maxwaste = 0
    # for i,j in row:
    # 	if j:
    # 		maxwaste += 1
    # maxwaste = math.ceil(capacity/j) * maxwaste
    # print(maxwaste)
    # donatelist = []
    # waste = 0
    # for i in range(len(grid)):
    # 	if grid[i][0]:
    # 		waste += grid[i][0]
    # 	if waste <= maxwaste:
    # 		donatelist.append(i)
    # 	else:
    # 		break

    bucket = -1
    before = 0
    count = 0
    for row in grid:
        for i, elem in enumerate(row):
            if elem:
                bucket += 1
                if bucket == capacity:
                    bucket = -1
                if bucket > before:
                    count += bucket - before
                    before = bucket
    return count
