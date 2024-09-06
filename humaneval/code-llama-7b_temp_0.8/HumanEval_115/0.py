
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
    def get_row_sum(row):
        """
        Returns the sum of the given row.
        """
        return sum(row)

    def get_bucket_usage(row_sum):
        """
        Returns the number of buckets required to extract the given number of units of water from the given row.
        """
        return math.ceil(row_sum / capacity)

    def get_bucket_usage_matrix(grid):
        """
        Returns a matrix of buckets required to empty each well.
        """
        # Get the number of rows
        num_rows = len(grid)
        # Get the number of columns in each row
        num_cols = len(grid[0])
        # Get the matrix of bucket usage for each well
        bucket_usage_matrix = [[0] * num_cols for _ in range(num_rows)]
        # Process each row in the grid
        for row_index, row in enumerate(grid):
            # Get the sum of the row
            row_sum = get_row_sum(row)
            # Get the number of buckets needed to empty the well
            bucket_usage = get_bucket_usage(row_sum)
            # Process each column in the row
            for col_index, col in enumerate(row):
                # Set the bucket usage in the matrix
                bucket_usage_matrix[row_index][col_index] = bucket_usage
        # Return the matrix of bucket usage for each well
        return bucket_usage_matrix

    def get_bucket_movements(bucket_usage_matrix):
        """
        Returns the number of buckets needed to empty each well.
        """
        # Get the number of rows
        num_rows = len(bucket_usage_matrix)
        # Get the number of columns
        num_cols = len(bucket_usage_matrix[0])
        # Process each row
        for row_index in range(num_rows):
            # Process each column
            for col_index in range(num_cols):
                # Check if this is the first column
                if col_index == 0:
                    # Check if this is the first row
                    if row_index == 0:
                
