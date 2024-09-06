
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
    #This function will return the maximum number of times that the bucket needs to be lowered.
    def max_fill(grid, capacity):
        # Additional variables to store the row and column count of the grid
        row_count = len(grid)
        col_count = len(grid[0])
        
        #An array to store the maximum number of times that the bucket needs to be lowered
        max_times = 0
        
        #An array to store the units of water present in each column.
        #This array will be zero indexed
        column_units = [0] * col_count
        
        #An array to store the number of times that the bucket needs to be lowered.
        #This array will be zero indexed
        times = [0] * col_count
        
        #A loop to calculate the maximum number of times that the bucket needs to be lowered.
        for row in grid:
            for col in range(col_count):
                if row[col] == 1:
                    column_units[col] += 1
            if max_times < max(times):
                max_times = max(times)
                
            times = [0] * col_count
                
        #Calculating the number of times that the bucket needs to be lowered.
        for unit in column_units:
            if unit > capacity:
                times[column_units.index(unit)] += math.ceil(unit / capacity)
                
        return max_times
    
    #Calling the function
    return max_fill(grid, capacity)
