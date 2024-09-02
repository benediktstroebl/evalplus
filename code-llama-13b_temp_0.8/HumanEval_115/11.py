
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
    num_rows = len(grid)
    num_columns = len(grid[0])
    num_buckets = 0
    num_operations = 0
    # Find the number of columns and rows that have a 1
    for i in range(num_rows):
        for j in range(num_columns):
            if grid[i][j] == 1:
                num_buckets += 1
    # We are going to fill each column with 1 bucket at a time.
    # We can use math.ceil(num_buckets / num_columns) iterations to fill all the columns.
    num_iterations = math.ceil(num_buckets / num_columns)
    for k in range(num_iterations):
        for i in range(num_rows):
            for j in range(num_columns):
                # If there is a 1 in the current row and column and the capacity
                # of the bucket isn't full, fill the bucket and continue to the next column.
                if grid[i][j] == 1 and num_buckets > 0:
                    grid[i][j] = 0
                    num_buckets -= 1
                    num_operations += 1
                    continue
                # If the bucket is full, we can pour it into the next well.
                if grid[i][j] == 0:
                    num_operations += 1
                    if j < (num_columns-1):
                        # If the next well in the same row is empty, pour the bucket into it.
                        if grid[i][j+1] == 0:
                            grid[i][j+1] = 1
                            num_buckets -= 1
                        # If the next well in the same row is full, check if the next well
                        # in the next row is full and pour the bucket into it.
                        elif grid[i][j+1] == 1:
                            if grid[i+1][j+1] == 1:
                                grid[i+1][j+1] = 0
                                num_buckets -= 1
                            else:
                               
