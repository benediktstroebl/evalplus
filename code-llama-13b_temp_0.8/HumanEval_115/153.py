
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

    def find_max_in_row(row):
        # Find the first 1 from the right in the row
        start = len(row) - 1
        while start >= 0 and row[start] == 0:
            start -= 1
        return start + 1

    def empty_well(well_length, bucket_capacity):
        # We use the same bucket for all the wells
        # The bucket starts empty
        bucket = 0
        steps = 0
        while bucket < well_length:
            # Fill the bucket
            bucket = min(well_length, bucket + bucket_capacity)
            # Empty the bucket
            bucket = max(0, bucket - bucket_capacity)
            steps += 1
        return steps

    # Find the first 1 in each row
    row_max_idx = []
    for row in grid:
        max_idx = find_max_in_row(row)
        if max_idx >= 0:
            row_max_idx.append(max_idx)
    # print(row_max_idx)

    # Find the maximum number of steps needed to empty the wells
    if not row_max_idx:
        return 0
    max_steps = math.inf
    for max_idx in row_max_idx:
        steps = empty_well(max_idx, capacity)
        # print(steps)
        max_steps = min(max_steps, steps)
    return max_steps

