
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
    # Write your code here
    max_row = len(grid)
    max_col = len(grid[0])
    num_buckets = math.ceil(max_row * max_col / capacity)
    grid_buckets = [[] for _ in range(num_buckets)]

    for i in range(max_row):
        for j in range(max_col):
            if grid[i][j] == 1:
                bucket_index = (i // max_row) * max_col + j
                grid_buckets[bucket_index].append((i, j))

    filled_buckets = [None] * num_buckets
    filled_buckets_count = [0] * num_buckets

    stack = []
    filled_buckets_count[0] = len(grid_buckets[0])
    stack.extend(grid_buckets[0])

    while stack:
        row, col = stack.pop()

        if filled_buckets[row] is None:
            filled_buckets[row] = col

        for neighbor in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            neighbor_row, neighbor_col = neighbor

            if 0 <= neighbor_row < max_row and 0 <= neighbor_col < max_col and grid[neighbor_row][neighbor_col] == 1 and filled_buckets[neighbor_row] is None:
                filled_buckets_count[neighbor_row] += 1
                stack.append(neighbor)

    total_buckets = 0
    for i in range(num_buckets):
        total_buckets += filled_buckets_count[i]

    return total_buckets - 1
