
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
    def max_buckets(grid, capacity):
        """
            very dumb solution - I think the trick is to find a way to calculate the water
            required to fill a specific column.
            I then work from left to right on the buckets.
        """
        # store the number of rows and columns in the grid
        nrow, ncol = len(grid), len(grid[0])
        # total number of wells
        nwells = nrow * ncol
        # calculate the maximum number of buckets that could be used
        max_buckets = min(nrow, ncol)
        # iterate through each bucket in the grid
        for i in range(max_buckets):
            # iterate through each column in the grid
            for j in range(ncol):
                # iterate through each row in the grid
                for k in range(nrow):
                    # calculate the number of water units required to fill the column
                    required_water = sum(grid[k][j:])
                    # if the required water is greater than the available water in the bucket
                    # then return that we cannot fill the column
                    if required_water > capacity: return -1
                    # if we have not reached the last row in the grid
                    # and the current row does not have enough water to fill the column
                    # skip to the next row
                    if k != nrow-1 and required_water > sum(grid[k+1][j:]): k += 1
                    # if we have enough water to fill the column
                    # return the number of times the buckets need to be lowered
                    if required_water == sum(grid[k][j:]):
                        return math.ceil(nwells / (i + 1))
        # return the number of times the buckets need to be lowered
        return math.ceil(nwells / max_buckets)

    def max_buckets_v2(grid, capacity):
        """
            better solution - don't need to iterate through each bucket in the grid
            for each column, calculate how much water is required to fill the column
            then iterate through the rows and see how many columns can be filled with
           
