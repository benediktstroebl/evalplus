import math
import collections
def max_fill(grid, capacity):
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
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
    num_rows = len(grid)
    num_cols = len(grid[0])

    if num_rows == 0 or num_cols == 0:
        return 0

    max_fetch = collections.deque()
    max_fetch.append(0)

    for col in range(num_cols):
        row_sum = 0
        for row in range(num_rows):
            row_sum += grid[row][col]
            max_fetch.append(row_fetch(row_sum, capacity, max_fetch))
        max_fetch.pop()

    return max_fetch[0]
def row_fetch(row_sum, capacity, max_fetch):
    remaining_capacity = capacity
    num_fetches = 0
    while remaining_capacity > 0 and row_sum > 0:
        if row_sum >= remaining_capacity:
            row_sum -= remaining_capacity
            num_fetches += 1
            remaining_capacity = 0
        else:
            num_fetches += 1
            remaining_capacity -= row_sum
            row_sum = 0
    max_fetch.append(num_fetches)
    return num_fetches
capacity = 1