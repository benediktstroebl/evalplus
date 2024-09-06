
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

    n_rows = len(grid)
    n_cols = len(grid[0])

    print(f"Grid: {grid}")
    print(f"Bucket Capacity: {capacity}")

    # Generate bucket and well pairs
    buckets = [(i, j) for i in range(n_rows) for j in range(n_cols)]
    print(f"Buckets: {buckets}")

    # Generate wells
    wells = [well for row in grid for well in row]
    print(f"Wells: {wells}")

    # Generate water to fill
    total_water = sum(wells)
    print(f"Total Water: {total_water}")

    # Generate amount of wells per row
    wells_per_row = [sum(row) for row in grid]
    print(f"Wells per Row: {wells_per_row}")

    # Calculate number of times to lower the bucket to empty wells
    # n_times = math.ceil(total_water / capacity)
    n_times = math.ceil(total_water / capacity) if total_water > capacity else 1
    print(f"Buckets lowered {n_times} times.")

    # Calculate amount of water per row on the last pass
    water_per_row = total_water % capacity if n_times > 1 else total_water
    print(f"Water per row: {water_per_row}")

    # Set up current well index
    well_idx = 0

    # Lower buckets
    for _ in range(n_times):

        print(f"-----------------")

        # Set up current bucket index
        bucket_idx = 0

        # Move over buckets in a single row
        for row_idx in range(n_rows):
            row_wells = wells_per_row[row_idx]
            print(f"Row: {row_idx}, wells: {row_wells}")

            # Move over buckets in a single row
            for _ in range(row_wells):
                print(
