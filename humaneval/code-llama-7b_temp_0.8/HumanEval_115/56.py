
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
    def find_max_bottles(grid, capacity):
        n_rows = len(grid)
        n_columns = len(grid[0])
        max_bottle_rows = [0] * (n_rows + 1)
        max_bottle_columns = [0] * (n_columns + 1)

        # Find max bottle
        for i in range(n_rows):
            for j in range(n_columns):
                if grid[i][j] == 1:
                    max_bottle_rows[i+1] = max_bottle_rows[i] + 1
                    max_bottle_columns[j+1] = max_bottle_columns[j] + 1
                else:
                    max_bottle_rows[i+1] = max_bottle_rows[i]
                    max_bottle_columns[j+1] = max_bottle_columns[j]

        return max(max_bottle_rows), max(max_bottle_columns)

    def calculate_needed(grid, bucket_capacity, max_bottle_rows, max_bottle_columns):
        n_rows = len(grid)
        n_columns = len(grid[0])

        needed = 0
        # Fill column by column
        for j in range(n_columns):
            for i in range(max_bottle_rows+1):
                needed += max(0, min(max_bottle_columns, max_bottle_columns-((n_rows-i) * bucket_capacity)) - grid[i][j])

        # Fill row by row
        for i in range(n_rows):
            for j in range(max_bottle_columns+1):
                needed += max(0, min(max_bottle_rows, max_bottle_rows-((n_columns-j) * bucket_capacity)) - grid[i][j])

        return needed

    # Find the maximum bottles
    max_bottle_rows, max
