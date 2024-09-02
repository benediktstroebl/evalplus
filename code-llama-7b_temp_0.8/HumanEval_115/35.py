
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

    n_rows, n_cols = len(grid), len(grid[0])
    visited = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    def get_lowest_index(grid, capacity, i, j):
        assert(grid[i][j] == 1)

        if (i, j) in visited:
            return 0

        visited[i][j] = 1

        n_filled = 1
        n_empty_wells = 0

        if i - 1 >= 0 and grid[i - 1][j] == 1:
            n_filled += get_lowest_index(grid, capacity, i - 1, j)
        
        if i + 1 < n_rows and grid[i + 1][j] == 1:
            n_filled += get_lowest_index(grid, capacity, i + 1, j)

        if j - 1 >= 0 and grid[i][j - 1] == 1:
            n_filled += get_lowest_index(grid, capacity, i, j - 1)

        if j + 1 < n_cols and grid[i][j + 1] == 1:
            n_filled += get_lowest_index(grid, capacity, i, j + 1)

        if n_filled > capacity:
            n_empty_wells = n_filled - capacity

        return n_empty_wells

    n_buckets_needed = 0
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                n_buckets_needed += math.ceil(get_lowest_index(grid, capacity, i, j) / capacity)

    return n_buckets_needed
