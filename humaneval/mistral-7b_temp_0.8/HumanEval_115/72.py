
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

    # 1 - initialize a counter
    counter = 0

    # 2 - iterate over the rows of the grid
    for row in range(len(grid)):
        # 3 - iterate over the columns of the current row
        for col in range(len(grid[0])):
            # 4 - check if the cell is empty (0)
            if grid[row][col] == 0:
                # 5 - if the cell is empty, keep track of the number of empty cells
                counter += 1

    # 6 - calculate the number of buckets needed to empty the grid
    buckets_needed = math.ceil(counter / capacity)

    # 7 - return the number of buckets needed
    return buckets_needed

