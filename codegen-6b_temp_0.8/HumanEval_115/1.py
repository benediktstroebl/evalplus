
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
    
    # flood fill
    # search for the first non-zero element
    # if not found, end
    # if non-zero, move one step forward filling the target well
    # if end, return
    # else, increase the size of the well by one step
    
    def can_fit(target_col, size):
        """
        We fit the target column if it is empty and we can fill the target column by size,
        and the target column is not full to the capacity
        """
        index = 0
        while index < len(grid) and grid[index][target_col] == 0 and grid[index][target_col+size] == 0:
            index += 1
        
        return index < len(grid)
    
    res = 0
    for row in grid:
        index = 0
        while index < len(row) and row[index] == 0:
            index += 1
        
        if index < len(row):
            while index < len(row) and row[index] == 0:
                if index + capacity - 1 < len(row):
                    #include all the wells
                    if can_fit(index, capacity):
                        return res
                else:
                    #we have to cut the row
                    return res
                index += 1
            
            res += 1
    return res
