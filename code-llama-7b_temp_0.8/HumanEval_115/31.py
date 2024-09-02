
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
    def get_max_water_till_position(grid, buckets, capacity):
        """
        Get max water that can be stored by filling buckets upto the current position
        """
        # Get the number of buckets required
        n_buckets_required = len(list(filter(lambda i: i[1] == 1, zip(range(len(grid)), grid[-1]))))
        # Get the maximum number of buckets that can be used
        max_buckets = min(n_buckets_required, len(buckets))
        # Set current capacity of buckets to 0
        for i in range(max_buckets):
            buckets[i] = 0

        # Calculate water
        water = 0
        for position, well in enumerate(grid[-1]):
            if well == 1:
                # Fill the bucket
                buckets[-1] += 1
                # Lower the bucket
                buckets[-1] = min(buckets[-1], capacity)
                # Get water in this well
                water += buckets[-1]
                # Fill the bucket
                buckets[-2] += 1
                # Lower the bucket
                buckets[-2] = min(buckets[-2], capacity)
                # Get water in this well
                water += buckets[-2]
        return water

    # Get the number of rows and columns
    n_rows, n_cols = len(grid), len(grid[0])
    # Initialise buckets to store water
    buckets = [0] * n_cols
    # Initialise a counter to count the number of times buckets were lowered
    lower_buckets = 0
    # Iterate over rows
    for row_index in range(n_rows - 1, -1, -1):
        # Get the max water that can be stored till the current row
        max_water_at_current_position = get_max_water_till_position(grid, buckets, capacity)
        # Get the maximum number of buckets that can be used to store water
        max_buckets_used = min(len(buckets), len(grid[row_index]))
       
