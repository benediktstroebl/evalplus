
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
    def get_min(grid):
        """
            returns the minimum number of buckets required to empty the grid
        """
        # 1. count all the 1's in each row
        # 2. find out the minimum length to cover all the 1's
        count = 0
        min_length = 0
        for row in grid:
            # for each row, find the number of 1's and update the count
            count += row.count(1)
            # find out the minimum length required to cover all the 1's
            min_length = max(min_length, len(row))
        # return the minimum length needed to cover all the 1's
        return min_length, math.ceil(count/min_length)
    
    def get_index(grid, index):
        """
            returns the index's element (i,j) in the grid
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == index:
                    return i, j
    
    # 1. find the minimum number of buckets required to empty the grid
    min_length, min_count = get_min(grid)
    # 2. the number of times we need to lower the buckets is equal to
    #     the number of buckets we need to empty the grid
    return min_count
