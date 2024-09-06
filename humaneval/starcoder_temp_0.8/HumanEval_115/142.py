
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
    # print(rows, cols)
    visited = [[False] * cols for _ in range(rows)]
    # print(visited)

    def fill(row, col):
        if visited[row][col]:
            return 0

        if grid[row][col] == 0:
            return float('inf')

        # print(row, col)
        # print(visited)
        # print(grid)
        visited[row][col] = True

        # right
        if col + 1 < cols:
            cost = fill(row, col + 1)
            if cost!= float('inf'):
                cost += 1

        # left
        if col - 1 >= 0:
            cost = fill(row, col - 1)
            if cost!= float('inf'):
                cost += 1

        # down
        if row + 1 < rows:
            cost = fill(row + 1, col)
            if cost!= float('inf'):
                cost += 1

        # up
        if row - 1 >= 0:
            cost = fill(row - 1, col)
            if cost!= float('inf'):
                cost += 1

        return cost

    # print(fill(0, 0))
    # print(fill(1, 1))
    return fill(0, 0)

