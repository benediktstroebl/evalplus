
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

    buckets = []
    num_of_rows = len(grid)
    num_of_columns = len(grid[0])
    for row in grid:
        for column in row:
            if column == 1:
                buckets.append((column, num_of_columns - 1, num_of_rows - 1))

    count = 0
    num_of_buckets = len(buckets)
    while num_of_buckets > 0:
        count += 1
        for i in range(num_of_buckets):
            if buckets[i][2] == 0:
                continue
            buckets[i][2] = buckets[i][2] - 1
            if buckets[i][0] + buckets[i][2] < capacity:
                continue
            elif buckets[i][0] + buckets[i][2] == capacity:
                buckets[i][0] = buckets[i][0] + buckets[i][2]
                buckets[i][2] = 0
                continue
            else:
                buckets[i][0] = capacity
                buckets[i][2] = buckets[i][2] - buckets[i][0]
                continue
        buckets.sort(key = lambda x: (-x[0], x[1], x[2]))

    return count
