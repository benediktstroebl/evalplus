
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
    # import math
    # def max_fill(grid, capacity):
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     left_to_right_filled = [[0 for _ in range(cols)] for _ in range(rows)]
    #     right_to_left_filled = [[0 for _ in range(cols)] for _ in range(rows)]
    #     # Find the rightmost column that has water in it
    #     rightmost_full_column = cols - 1
    #     while rightmost_full_column > 0 and not any(grid[row][rightmost_full_column] for row in range(rows)):
    #         rightmost_full_column -= 1
    #     # Fill up from rightmost column to left
    #     for row in range(rows):
    #         current_column = rightmost_full_column
    #         while current_column >= 0:
    #             if grid[row][current_column]:
    #                 left_to_right_filled[row][current_column] = capacity
    #             current_column -= 1
    #     # Find the leftmost column that has water in it
    #     leftmost_full_column = 0
    #     while leftmost_full_column < cols - 1 and not any(grid[row][leftmost_full_column] for row in range(rows)):
    #         leftmost_full_column += 1
    #     # Fill up from leftmost column to right
    #     for row in range(rows):
    #         current_column = leftmost_full_column
    #         while current_column <= cols - 1:
    #             if grid[row][current_column]:
    #                 right_to_left_filled[row][current_column] = capacity
    #             current_column += 1
    #     # Let's try to find the minimum number of operations needed to fill up the wells
    #     operations = 0
    #     # Calculate how many times we would need to fill up a certain row to fill up all the wells
    #     for row in range(rows):
    
