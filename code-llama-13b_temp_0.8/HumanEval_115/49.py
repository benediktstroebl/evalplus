
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
    
    def water_collected(grid, r, c, capacity):
        """
        Returns the number of times the bucket needs to be emptied
        given a starting position in the grid, a capacity, and a grid.
        """
        if capacity == 0:
            return 0

        def try_collect(n):
            """
            Tries to collect n units of water and returns True if successful.
            """
            # Make sure n doesn't exceed capacity.
            n = min(n, capacity)
            # Make sure n doesn't exceed well capacity.
            n = min(n, grid[r][c])
            # Try to collect n units of water.
            grid[r][c] -= n
            # Go to the left and try to collect.
            left_start_row = r
            while left_start_row >= 0 and grid[left_start_row][c] >= 0:
                collected = try_collect(n)
                if collected:
                    return True
                left_start_row -= 1
            # Go to the right and try to collect.
            right_start_row = r
            while right_start_row < len(grid) and grid[right_start_row][c] >= 0:
                collected = try_collect(n)
                if collected:
                    return True
                right_start_row += 1
            # Go up and try to collect.
            up_start_col = c
            while up_start_col >= 0 and grid[r][up_start_col] >= 0:
                collected = try_collect(n)
                if collected:
                    return True
                up_start_col -= 1
            # Go down and try to collect.
            down_start_col = c
            while down_start_col < len(grid[r]) and grid[r][down_start_col] >= 0:
                collected = try_collect(n)
                if collected:
                    return True
                down_start_col += 1
            return False

        # Try to collect as much as possible.
        return try_collect(math.inf)

    # Initialize
