
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

    # Grid with locations
    grid_with_locations = []
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 0:
                continue
            grid_with_locations.append((i, j))

    # Grid without locations
    grid_without_locations = []
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 0:
                continue
            grid_without_locations.append(0)

    # Empty buckets
    buckets = []
    for _ in range(capacity):
        buckets.append(0)

    # Fill the buckets
    n_moves = 0
    while grid_with_locations:
        n_moves += 1
        # Move the water
        for i, j in grid_with_locations:
            # Decrease the water level
            grid_without_locations[i * n_cols + j] -= 1
            # Move the water
            buckets[grid_without_locations[i * n_cols + j]] += 1

        # Empty the buckets
        n_empty_buckets = 0
        for i in range(len(buckets)):
            if buckets[i] == 0:
                continue
            buckets[i] -= 1
            n_empty_buckets += 1

        # Add new locations
        for _ in range(n_empty_buckets):
            new_i, new_j = grid_with_locations.pop()
            # Update the grid
            grid_without_locations[new_i * n_cols + new_j] += 1
            # Add new location
            new_k = math.floor(grid_without_locations[new_i * n_cols + new_j])
            grid_with_locations.append((new_i, new_k))

    return n_moves


