
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
    # Run time: O(n^2) | Space: O(n^2)
    # Bucket capacity is 1
    # Idea:
    # - Create a copy of grid with 1's and -1's.
    # - For each row:
    #     - Starting from the leftmost 1, count the number of 1's in this row.
    #     - Multiply this number with the number of 1's in the column.
    #     - This is the number of buckets needed to fill this cell.
    # - Sum up all of these numbers. This is the number of times we need to lower the buckets.
    #
    # Bucket capacity is 2
    # Idea:
    # - Create a copy of grid with 1's and -1's.
    # - For each row:
    #     - Starting from the leftmost 1, count the number of 1's in this row.
    #     - Multiply this number with the number of 1's in the column.
    #     - This is the number of
