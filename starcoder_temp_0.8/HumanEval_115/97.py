
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
    # return 0
    import math
    rows, cols = len(grid), len(grid[0])
    # find max row index
    max_row, max_col = 0, 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                max_row, max_col = row, col

    # BFS
    q = [(0, max_row, max_col)]
    visited = set([(0, max_row, max_col)])
    level = 0
    # count = 0
    while q:
        level += 1
        # count += 1
        size = len(q)
        for _ in range(size):
            # start from q.pop(0)
            depth, row, col = q.pop(0)
            # when found the right answer
            if depth == capacity:
                return level
            # get four directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                # if r == max_row and c == max_col:
                #     break
                if (r < 0 or r >= rows or c < 0 or c >= cols or
                        (r, c) in visited or grid[r][c] == 0):
                    continue
                visited.add((r, c))
                q.append((depth + 1, r, c))
