
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

    r, c = len(grid), len(grid[0])
    visited = set()
    visited.add((0,0))
    level = 0
    queue = deque([(0,0)])
    while queue:
        row, col = queue.popleft()
        for x in (0, 1):
            for y in (0, 1):
                new_row, new_col = row + x, col + y
                if 0 <= new_row < r and 0 <= new_col < c:
                    if not (new_row, new_col) in visited:
                        visited.add((new_row, new_col))
                        if grid[new_row][new_col] == 1:
                            queue.append((new_row, new_col))

    if level == 0:
        return 0
    else:
        return math.ceil(r * c / float(capacity))

    pass

