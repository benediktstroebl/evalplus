
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
    def to_zeros(grid, bucket_capacity):
        """
        This function turns the 1s in the grid into 0s and
        calculates the number of times you need to lower the buckets.
        """
        count = 0
        # Iterate through each row
        for row in range(len(grid)):
            # Iterate through each column
            for column in range(len(grid[row])):
                # If the current cell is 1
                if grid[row][column] == 1:
                    # Subtract the current cell value from the bucket capacity
                    grid[row][column] -= bucket_capacity
                    # Increment the count of bucket lowers
                    count += 1
                    # If the current cell is still equal to 0
                    if grid[row][column] == 0:
                        # Check if the previous cell is also 0
                        if grid[row][column-1] == 0:
                            # Set the previous cell to 1
                            grid[row][column-1] = 1
                        #
