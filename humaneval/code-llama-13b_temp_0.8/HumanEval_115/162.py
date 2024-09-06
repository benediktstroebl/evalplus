
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

    n = len(grid)
    m = len(grid[0])

    # total units of water to empty out
    water_to_be_emptied = sum(grid[i][j] for i in range(n) for j in range(m))

    # initial fill
    # Number of full buckets at the start
    full_buckets = math.floor(water_to_be_emptied / capacity)
    units_to_be_emptied = water_to_be_emptied - (full_buckets * capacity)
    full_buckets_to_return = full_buckets

    # emptying the remaining units
    for i in range(n):
        # start with the last row
        row = n - 1 - i
        for j in range(m):
            # start with the last column
            col = m - 1 - j
            # if the bucket is already full, it is better to leave it in this
            # position and move to the next column
            if grid[row][col] == capacity:
                continue
            else:
                # move to the left
                if j + grid[row][col] > capacity and (j + grid[row][col]) - capacity != 1:
                    # if the next cell has no water, there is no need to move the
                    # bucket, just move to the next column
                    if row + 1 < n and grid[row + 1][col] == 0:
                        units_to_be_emptied -= capacity - grid[row][col]
                        full_buckets_to_return += 1
                        continue
                    # otherwise move to the next row
                    else:
                        units_to_be_emptied -= capacity - grid[row][col]
                        full_buckets_to_return += 1
                        row += 1
                        continue
                # move to the right
                if col + grid[row][col] > capacity and (col + grid[row][col]) - capacity != 1:
                    # if the next cell has no water, there is no need to move the
                    # bucket, just move to the next column
                
