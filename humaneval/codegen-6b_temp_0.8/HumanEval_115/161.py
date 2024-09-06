
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
    # rows, cols = len(grid), len(grid[0])
    # def min_steps(row, col):
    #     if row == rows-1:
    #         return row * cols - capacity
    #     if col == cols-1:
    #         return min_steps(row+1, 0)
    #     return min(min_steps(row+1, col), min_steps(row, col+1))

    # return min_steps(0, 0)

    import math
    rows, cols = len(grid), len(grid[0])

    def min_steps(row, col):
        if row == rows-1:
            return min(capacity, col)
        if col == cols-1:
            return min_steps(row+1, 0)
        p_i, l_i = min(min_steps(row+1, col), min_steps(row, col+1))
        if grid[row][col] == 1:
            return p_i
        return l_i

    def print_grid(grid):
        for row in grid:
            print(row, end="")
        print()

    print_grid(grid)
    return min_steps(0, 0)

