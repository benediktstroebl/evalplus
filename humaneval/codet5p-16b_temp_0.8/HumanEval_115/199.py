
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

    def find_wells(grid, capacity):
        width, height = len(grid[0]), len(grid)
        nodes = []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    nodes.append((i, j))

        def dfs(i, j, visited, nodes, capacity, grid, bucket):
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= ni < height and 0 <= nj < width and not (ni, nj) in visited and grid[ni][nj] == 1:
                    visited.add((ni, nj))
                    dfs(ni, nj, visited, nodes, capacity, grid, bucket + 1)
                    visited.remove((ni, nj))
                else:
                    continue

        def find_wells_helper(nodes, capacity, grid):
            max_buckets = 0
            visited = set()
            for
