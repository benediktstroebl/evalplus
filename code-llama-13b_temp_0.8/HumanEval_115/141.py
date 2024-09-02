
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
    total_water = sum([sum(x) for x in grid])
    if total_water < capacity:
        return 0

    def count_water(grid, capacity):
        """
        Counts the number of times that we need to lower the bucket
        to fill the wells with the given capacity.
        """
        rows = len(grid)
        cols = len(grid[0])
        bucket_capacity = capacity

        # Number of times we need to lower the bucket to fill the wells with the given capacity.
        bucket_count = 0

        # Iterate through each row
        for i in range(rows):
            # Iterate through each col
            for j in range(cols):
                # Only process the water cells.
                if grid[i][j] == 1:
                    # Check if there is space to fill the bucket with water.
                    if j + bucket_capacity <= cols:
                        # Check if there is enough water to fill the bucket.
                        if sum(grid[i][j:j+bucket_capacity]) >= bucket_capacity:
                            # Fill the bucket.
                            for k in range(bucket_capacity):
                                grid[i][j+k] = 0
                            # Increase the bucket count.
                            bucket_count += 1
                    else:
                        # Check if there is enough water to fill the bucket.
                        if sum(grid[i][j:]) >= bucket_capacity:
                            # Fill the bucket.
                            for k in range(cols - j):
                                grid[i][j+k] = 0
                            # Increase the bucket count.
                            bucket_count += 1
        return bucket_count

    # Starting bucket capacity
    current_capacity = 1

    # Keep lowering the bucket capacity until it is filled.
    while count_water(grid, current_capacity) < math.inf:
        current_capacity += 1
    return current_capacity - 1
