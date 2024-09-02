
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
    n_wells = len(grid)
    total_wells = sum([sum(x) for x in grid])
    bucket_usage = total_wells // capacity

    while bucket_usage != 0:
        bucket = capacity
        used_wells = 0

        # We have used all the water, no need to empty the bucket
        if bucket_usage == 0:
            break

        # If we can empty the bucket on the same row, we do so, and then move on to the next row
        for row in grid:
            if len(row) - row.count(0) < bucket:
                used_wells += len(row) - row.count(0)
                bucket -= len(row) - row.count(0)
                row = [0 for _ in row]

        # If not, we fill the remaining water in the last row
        if bucket != capacity:
            last_row = grid[-1]
            last_row = [1 if x < bucket else 0 for x in last_row]
            bucket -= sum(last_row)

            # In case we can't fill the bucket, the remaining water will be in the last row
            grid[-1] = last_row

        # The remaining buckets are the remaining wells we need to empty
        bucket_usage = total_wells - used_wells

    return math.ceil(total_wells / capacity)

