
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
    import math
    # Find the maximum row length
    max_row_length = max([len(row) for row in grid])

    # Add padding to the end of each row such that all rows are the same length
    for row in grid:
        while len(row) < max_row_length:
            row.append(0)

    # Calculate the number of buckets required
    num_buckets = int(math.ceil(max_row_length / capacity))

    # Construct the buckets
    buckets = []
    for i in range(num_buckets):
        buckets.append([])

    # Iterate through all of the rows
    for row in grid:
        # Iterate through the row
        for i in range(len(row)):
            # If the current position is empty, skip
            if row[i] == 0:
                continue

            # Find the index of the bucket to which this water belongs
            bucket_index = int(i / capacity)

            # If the bucket is not full, add the current position to the bucket
            if len(buckets[bucket_index]) < capacity:
                buckets[bucket_index].append(i)
            # If the bucket is full, add the current position to the top of the bucket
            else:
                buckets[bucket_index].insert(0, i)

    # Iterate through all of the buckets
    for bucket in buckets:
        # Iterate through all of the positions in the bucket
        for i in range(len(bucket)):
            # Extract the current position
            position = bucket[i]

            # Iterate through all of the positions in the bucket that come after this position
            for j in range(i + 1, len(bucket)):
                # Extract the next position
                next_position = bucket[j]

                # If the current position is lower than the next position, swap them
                if position < next_position:
                    bucket[j], bucket[i] = bucket[i], bucket[j]

    # Iterate through all of the buckets
    for bucket in buckets:
        # Iterate through all of the positions in the bucket
