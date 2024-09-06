
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
    # TODO: find a faster algorithm
    def find_highest_row(grid, col):
        """
        Return highest row index that has 1 at column 'col'.
        """
        for row in reversed(range(len(grid))):
            if grid[row][col] == 1:
                return row
        return None

    def find_lowest_row(grid, col):
        """
        Return lowest row index that has 1 at column 'col'.
        """
        for row in range(len(grid)):
            if grid[row][col] == 1:
                return row
        return None

    def solve(grid, capacity):
        """
        Note: you cannot use any extra space.
        """
        raise NotImplementedError

    def solve_slow(grid, capacity):
        """
        A very naive solution.
        """
        import math

        # Find the longest well in the grid.
        max_well_width = max(len(row) for row in grid)

        # Create a bucket.
        bucket = [0] * capacity

        # Count the number of times we lowered the bucket.
        count = 0

        # Find the highest row in each well.
        highest_row_in_each_well = []
        for i in range(len(grid[0])):
            highest_row_in_each_well.append(find_highest_row(grid, i))

        # Empty the wells.
        for col in range(max_well_width):
            # Find the highest row with a well at 'col'.
            # This is the bucket's location.
            highest_row = highest_row_in_each_well[col]

            # Find the lowest row with a well at 'col'.
            lowest_row = find_lowest_row(grid, col)

            # Find the number of units in the well at 'col'.
            # This is the bucket's fill.
            fill = lowest_row - highest_row

            # If the bucket's fill is greater than the bucket's capacity, we need to empty the well.
            if fill >
