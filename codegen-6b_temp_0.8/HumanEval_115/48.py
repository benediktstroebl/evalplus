
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
    def bucket_count(grid, capacity):
        rows, columns = len(grid), len(grid[0])
        res = [[[] for _ in range(columns)] for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                # remember the capacity for the well i,j
                res[i][j].append(grid[i][j])
                # lower the bucket capacity each time
                delta = min(capacity, grid[i][j])
                capacity -= delta
                # count the number of times we empty the bucket
                res[i][j].append(math.ceil(delta / capacity))

        for i in range(rows):
            for j in range(columns):
                res[i][j].sort()

        for i in range(rows):
            for j in range(columns):
                if len(res[i][j]) == 2:
                    # we empty the bucket
                    res[i][j][1] += 1
        return res

    grid = bucket_count(grid, capacity)

    # find min and max of the grid
    min_v = min(row.pop() for row in grid)
    max_v = max(row.pop() for row in grid)

    # see if we can empty all of the entries
    if max_v == 0:
        return 0
    return 1 + (max_v - min_v) - 1

