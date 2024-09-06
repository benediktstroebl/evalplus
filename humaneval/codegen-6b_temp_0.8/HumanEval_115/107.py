
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
    
    rows, cols = len(grid), len(grid[0])
    
    grid = [i + [0] * (cols - len(i)) for i in grid]

    for i in range(rows):
        grid[i] += ([0] * (capacity + 1))

    def adjacent_wells(row, col):
        for i in kernel:
            for j in kernel:
                if row + i >= 0 and row + i < rows:
                    if col + j >= 0 and col + j < cols:
                        yield grid[row + i][col + j]

    kernel = [[-1, 1], [0, 1]]

    result = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                result += 1
                queue = [(row, col)]
                while queue:
                    i, j = queue.pop(0)
                    grid[i][j] = 0
                    for a in adjacent_wells(i, j):
                        if a:
                            queue.append((i + row, j + col))

    return result

