
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
    # sorting the grid
    grid.sort(key=lambda x: x[0])

    # store the number of times we need to lower the bucket for each row
    row_count = [0] * len(grid)
    # mark the grid as visited
    grid_visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    bucket_visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # find the maximum capacity of a well
    capacity_max = max(grid[0])
    # find the number of rows with a capacity of 0
    zero_rows = sum([row == capacity_max for row in grid])
    # if there are zero rows, return 0
    if zero_rows == len(grid):
        return 0

    while len(row_count) < len(grid):
        # loop through all rows
        for i in range(len(grid)):
            if not row_count[i]:
                # if the current row is empty, check if the previous row was full
                j = i - 1
                while j >= 0 and row_count[j] > 0:
                    # if the previous row was full, subtract the capacity of the current row from the previous row
                    row_count[j] -= grid[i][0]
                    bucket_visited[i][0] = False
                # if the previous row was not full, the current row is the first to be filled
                bucket_visited[i][0] = True
                # mark the current row as visited
                grid_visited[i][0] = True
            else:
                # if the current row has water, check if the next row has enough capacity to take water
                j = i + 1
                while j < len(grid) and row_count[j] < grid[i][0]:
                    # if the next row has enough capacity, subtract the capacity of the current row from the next row
                    row_count[j] -= grid[i][0]
                    bucket_visited[i][0] = False
                    bucket_visited
