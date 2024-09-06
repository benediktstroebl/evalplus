
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
    # Maximum capacity of a bucket = 100
    # Maximum number of buckets = 100
    # So, for this problem, we'll just use an array of size 101 (for a bucket capacity of 10)
    # And we'll store the number of full buckets
    buckets = [0 for _ in range(capacity + 1)]
    bucket_count = 0

    # First, go through each row
    for row in grid:
        bucket_count = max(bucket_count, math.floor(sum(row) / capacity))

        # Then, for each bucket, fill it with the corresponding water
        for i, x in enumerate(row):
            buckets[x] += 1

            # Check if we should empty it
            if buckets[x] > bucket_count:
                # Empty the bucket
                buckets[x] -= 1

                # Check if we've emptied all the buckets
                if sum(buckets) == 0:
                    # Reset the number of full buckets
                    bucket_count = 0
                else:
                    # Find the next filled bucket
                    bucket_count = buckets.index(max(buckets))
                    break

    return bucket_count

