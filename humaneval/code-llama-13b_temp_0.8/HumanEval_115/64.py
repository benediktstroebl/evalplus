
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
    # #Initialization
    # grid_copy = grid.copy()
    # #Traverse the grid row by row from top to bottom.
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         #Traverse the grid column by column from left to right.
    #         for k in range(j, len(grid[0])):
    #             #If the capacity is greater than or equal to the number of water units, then fill up the bucket.
    #             if (k-j)+1 <= capacity:
    #                 #Fill the bucket with the number of water units in the current column.
    #                 grid_copy[i][k] = (grid[i][j] * (k-j+1))
    #                 #Decrease the water units in the current column.
    #                 grid[i][j] = 0
    #             #If the capacity is less than the number of water units, then fill up the bucket
    #             #with the capacity units of water.
    #             else:
    #                 grid_copy[i][j] = capacity * grid[i][j]
    #                 #Decrease the water units in the current column by the capacity units.
    #                 grid[i][j] = grid[i][j] - capacity
    #                 #Exit the loop because the bucket has been filled.
    #                 break
    # #Sum up the water units in all the wells.
    # res = sum([sum(x) for x in grid_copy])
    # return res

    grid_copy = grid.copy()
    # Traverse the grid row by row from bottom to top.
    for i in range(len(grid)-1, -1, -1):
        # Traverse the grid column by column from left to right.
        for j in range(len(grid[0])):
            # Traverse the grid column by column from right to left.
            for k in range(len(grid[0])-1, j-1, -1):
                # If the capacity is greater than or equal to the number of water units, then fill up the bucket.
                if (k-j
