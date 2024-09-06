
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
    # write your code here
    def bucket_count(grid, capacity):
        visited = set()
        empty = 0
        total = 0
        while True:
            new_visited = set()
            for x, row in enumerate(grid):
                for y, cell in enumerate(row):
                    if cell == 1 and (x, y) not in visited:
                        total += 1
                        tmp_visited = set()
                        for i in range(x-1, x+2):
                            for j in range(y-1, y+2):
                                if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and (i, j) not in visited and (abs(i-x) + abs(j-y)) <= 1:
                                    tmp_visited.add((i, j))
                        for i in tmp_visited:
                            new_visited.add(i)
                        if grid[x][y] == 1:
                            grid[
