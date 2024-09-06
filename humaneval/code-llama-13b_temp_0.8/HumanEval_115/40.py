
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
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_wells = num_rows*num_cols
    # init buckets
    bucket_capacity = capacity
    buckets_amount = math.ceil(num_wells/bucket_capacity)
    # init results
    results = []
    for i in range(buckets_amount):
        # init row
        result_row = []
        for j in range(num_cols):
            # init col
            result_col = []
            # init bucket
            bucket_result = []
            # init bucket cursor
            bucket_cursor = bucket_capacity
            # init bucket size
            bucket_size = 0
            # init well cursor
            well_cursor = 0
            # fill bucket
            while well_cursor < num_wells and bucket_cursor > 0:
                # init current well
                well = grid[well_cursor//num_cols][well_cursor%num_cols]
                # increment well cursor
                well_cursor += 1
                # if well is avalible
                if well > 0:
                    # increment bucket size
                    bucket_size += 1
                # decrement bucket cursor
                bucket_cursor -= 1
                # if bucket is full
                if bucket_cursor == 0:
                    # append bucket result
                    bucket_result.append(bucket_size)
                    # reset bucket cursor
                    bucket_cursor = bucket_capacity
                    # reset bucket size
                    bucket_size = 0
            # append bucket result
            result_col.append(bucket_result)
        # append row result
        results.append(result_col)
    return results


