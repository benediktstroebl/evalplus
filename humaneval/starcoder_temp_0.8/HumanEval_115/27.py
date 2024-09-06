
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
    rows = len(grid)
    cols = len(grid[0])

    # record the maximum flow from the bottom row up
    # the maximum flow from the bottom row up is the number of 1's in the grid
    # with a capacity of capacity, it is 1
    flow = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows-1):
        for j in range(cols):
            if grid[i][j] and grid[i+1][j]:
                flow[i][j] = 1

    # use a stack to store the rows in the order of decreasing flow
    stack = []
    for i in range(rows-1):
        stack.append(i)

    # iteratively push rows of flow to the bottom
    for i in range(rows-1):
        row = stack.pop()
        for j in range(cols):
            # if the row is not in the stack, and the cell can flow down, 
            # then push the row to the stack
            if not grid[row][j] and flow[row][j] and row < rows-1:
                stack.append(row)
                break

    # calculate the max flow by getting the maximum flow from the bottom up
    # and multiplying it by the bucket capacity to get the number of times
    # the buckets need to be filled
    max_flow = 0
    for i in range(rows-1):
        max_flow += flow[i][:]

    return max_flow*capacity

