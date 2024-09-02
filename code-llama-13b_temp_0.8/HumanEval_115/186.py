
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
    # test cases
    # print(max_fill(grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]], capacity = 1))
    # print(max_fill(grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], capacity = 2))
    # print(max_fill(grid = [[0,0,0], [0,0,0]], capacity = 5))

    # initialize variables
    rows = len(grid)
    columns = len(grid[0])

    # to keep track of the maximum number of wells filled
    # in the current iteration
    max_num_wells = -math.inf

    # we go through all possible buckets
    for i in range(1, capacity+1):

        # we need to keep track of how many wells
        # we are filling with the current bucket
        num_wells = 0

        # we go through each row
        for row in range(rows):

            # we need to keep track of how many columns we have
            # filled with the current bucket
            # and if the bucket can still fill more columns
            # in the current row
            column = 0
            full = False

            # we go through each column
            while column < columns:

                # if the current bucket cannot fill
                # the entire remaining row
                if i < columns-column:
                    
                    # we fill the maximum number of columns
                    # that the current bucket can
                    for j in range(i):

                        # if we encounter a water unit
                        if grid[row][column] == 1:
                            num_wells += 1
                            
                            # we mark it as filled
                            grid[row][column] = 0

                        # increment the column counter
                        column += 1

                    # we have filled the entire bucket
                    full = True
                    break
                
                else:
                    
                    # we fill the entire remaining row
                    for j in
