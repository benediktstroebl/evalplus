
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
    n_rows = len(grid)
    n_cols = len(grid[0])

    def bfs(grid, n_rows, n_cols):
        queue = deque()
        visited = set()
        depth = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    queue.append((r, c))
                    visited.add((r, c))

        while queue:
            n = len(queue)
            depth += 1

            for _ in range(n):
                x, y = queue.popleft()

                for r, c in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if (
                        0 <= r < n_rows
                        and 0 <= c < n_cols
                        and grid[r][c] == 1
                        and (r, c) not in visited
                    ):
                        visited.add((r, c))
                        queue.append((r, c))

        return depth

    return bfs(grid, n_rows, n_cols) - math.ceil(n_rows * n_cols / capacity)

