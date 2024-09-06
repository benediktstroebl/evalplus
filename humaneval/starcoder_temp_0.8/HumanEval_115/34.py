
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
    if capacity == 0:
        return 0
    if capacity == 1:
        return sum([1 for row in grid for col in row if col == 1])

    rows = len(grid)
    cols = len(grid[0])
    # Buckets
    buckets = [[] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # If we have a bucket to fill
                if buckets[i]:
                    # Fill the bucket
                    buckets[i][-1].append(j)
                # If we don't have a bucket to fill
                else:
                    # Create a new bucket
                    buckets[i].append([j])

    # Go through each bucket
    # Keep track of the number of times we need to lower the bucket
    result = 0
    for bucket in buckets:
        # If there are multiple buckets to fill
        if len(bucket) > 1:
            # Go through each bucket
            # Keep track of the starting point
            start = 0
            # For each bucket, we want to fill it up to its capacity
            # Once the bucket is full, we need to lower it and move on
            for i in range(len(bucket)):
                if sum(bucket[i]) > capacity:
                    result += 1
                    start = i + 1
                    break
            # If we filled at least one bucket
            if start > 0:
                # Lower the buckets
                bucket = bucket[start:]
                # Keep track of the total number of units we have left to fill
                units = capacity - sum(bucket[0])
                # Create a list of indices that we want to fill with water
                # We want to fill the bucket until its capacity is satisfied
                # But we also want to make sure that the bucket is filled in
                # Individually. For example, if there is 1 unit left to fill and the
                # bucket is 3 units, we want to fill 2 units with the first two indices
                # and fill the 3rd index with one unit.
                indices = []
                for i in range(len(bucket)):
                    # If there are still units left to fill
                    if units > 0:
                        # Fill the bucket
                        indices += bucket[i]
                        # Decrement the units we have left to fill
                        units -= 1
                    # If there are no more units left to
