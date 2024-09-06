
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

    # 1. get the size of the grid
    row, col = len(grid), len(grid[0])
    # 2. if the grid is empty or the capacity is 0, just return 0
    if row == 0 or capacity == 0:
        return 0
    # 3. go through each row
    for i in range(row):
        # 4. go through each element in the row
        for j in range(col):
            # 5. if the element in the row is 1
            if grid[i][j] == 1:
                # 6. find the lowest accessible bucket
                bucket = get_lowest_bucket(grid, i, j, capacity)
                # 7. if the lowest accessible bucket is None, then return 0
                if bucket is None:
                    return 0
    # 8. return the number of times that we have to use the buckets
    return bucket["num_fill"]
