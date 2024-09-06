
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
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    if rows == 1:
        return sum(grid[0])
    #print('rows', rows, 'cols', cols, 'capacity', capacity)
    #print('grid', grid)
    
    # 1. collect the total units of water in the grid
    total_units = 0
    for row in grid:
        for col in row:
            if col:
                total_units += col
    #print('total units', total_units)

    # 2. prepare the answer
    result = []

    # 3. find the largest rectangle for each row
    for row in range(rows):
        # initialize the answer for this row
        result.append(0)

        # find the largest rectangle for this row
        heights = [0] * cols
        for col in range(cols):
            if grid[row][col]:
                heights[col] = grid[row][col]
        #print('heights', heights)

        # find the largest rectangle in the row using largestRectangleBottom
        #widths = [1] * cols
        #print('widths', widths)
        #area = largestRectangleBottom(heights, widths)
        #result[row] = area
        result[row] = largestRectangleBottom(heights)
    #print('result', result)

    # 4. calculate the maximum fill
    max_fill = 0
    for row in range(rows):
        max_fill += min(capacity, result[row] / rows)
    #print('max_fill', max_fill)

    # 5. calculate the number of times we need to lower the buckets
    # we need to lower the buckets the total number of times we can lower the buckets
    # divided by the capacity
    return math.ceil(total_units / max_fill)
