
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

    # TODO: implement max_fill
    # first approach: loop through every cell in the grid and check if the cell has water
    # if it does, add it to a list of wells and then iterate through the list and fill the buckets
    # with as much water as possible until the bucket is full or there is no more water in the well
    # if there is no more water in the well, remove the well from the list and go to the next one
    # return the number of times the buckets were filled

    # second approach: loop through every cell in the grid and check if the cell has water
    # if it does, add it to a list of wells and then iterate through the list and fill the buckets
    # with as much water as possible until the bucket is full or there is no more water in the well
    # if there is no more water in the well, remove the well from the list and go to the next one
    # return the number of times the buckets were filled

    # third approach: loop through every cell in the grid and check if the cell has water
    # if it does, add it
