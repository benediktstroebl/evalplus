
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
    print(grid)
    print(capacity)

    # The number of wells
    n_wells = len(grid)

    # The number of buckets
    n_buckets = n_wells

    # The number of turns
    n_turns = 0

    # The maximum number of wells filled in a turn
    max_filled_in_a_turn = 0

    # The maximum number of wells filled in a turn for a given capacity
    max_filled_in_a_turn_capacity = 0

    while n_buckets != 0:
        n_filled = 0

        for i in range(n_wells):
            if grid[i].count(1) > max_filled_in_a_turn_capacity:
                max_filled_in_a_turn_capacity = grid[i].count(1)

            if grid[i].count(1) > max_filled_in_a_turn:
                n_filled += grid[i].count(1)

        # Increase the number of turns
        n_turns += 1

        # Increase the number of buckets
        n_buckets -= 1

        # Decrease the number of wells filled in a turn
        max_filled_in_a_turn = max_filled_in_a_turn_capacity

        # Empty the current row
        for i in range(n_wells):
            # Decrease the number of filled wells
            n_filled -= grid[i].count(1)

            # Empty the well
            grid[i] = [0 for _ in range(len(grid[i]))]

        # If there are still filled wells
        if n_filled != 0:
            # Increase the number of buckets
            n_buckets += 1

    # Output the number of turns
    return n_turns

