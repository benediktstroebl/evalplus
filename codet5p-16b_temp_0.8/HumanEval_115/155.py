
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

    def _helper(grid, bucket_capacity):
        def _bfs(grid, bucket_capacity, node_idx):
            queue = [(node_idx, 0)]
            visited = set([node_idx])
            while queue:
                curr_idx, curr_level = queue.pop(0)
                for neighbor in [(curr_idx + 1, curr_level + 1), (curr_idx - 1, curr_level + 1)]:
                    if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and neighbor[0]!= curr_idx and neighbor[1]!= curr_idx and neighbor not in visited:
                        if grid[neighbor[0]][neighbor[1]] == 0:
                            visited.add(neighbor)
                            queue.append(neighbor)
            return curr_level
        max_level = -math.inf
        for row_idx, row in enumerate(grid):
            for col_idx, elem
