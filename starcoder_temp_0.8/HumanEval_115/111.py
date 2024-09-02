
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

    def _max_fill(row, col, depth, visited, bucket_capacity):
        # 0. Check if bucket_capacity has been reached
        if row == len(grid) or col == len(grid[row]) or depth == bucket_capacity:
            return depth
        # 1. Mark as visited
        visited[row][col] = True

        # 2. Get the best next move
        best_move = depth
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r == row and c == col:
                    continue
                if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[row]) and not visited[r][c]:
                    best_move = max(best_move, _max_fill(r, c, depth + 1, visited, bucket_capacity))

        # 3. Unmark as visited
        visited[row][col] = False
        return best_move

    # 0. If bucket_capacity is 0, return 0
    if bucket_capacity == 0:
        return 0

    # 1. Get the starting point
    visited = [[False for _ in grid[0]] for _ in grid]
    starting_point = None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                starting_point = (row, col)
                break
        if starting_point:
            break

    # 2. Start the depth-first-search
    return _max_fill(*starting_point, 0, visited, bucket_capacity)

