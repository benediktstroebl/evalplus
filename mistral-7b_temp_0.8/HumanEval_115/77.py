
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
    # Code here
    # Time: O(n^2)
    # Space: O(n^2)
    rows = len(grid)
    cols = len(grid[0])
    direction = 'down'
    bucket_count = 0
    rows_to_fill = set()
    visited = set()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                rows_to_fill.add(i)

    while rows_to_fill:
        if direction == 'down':
            rows_to_fill.discard(0)
            for row in rows_to_fill:
                for j in range(cols):
                    if grid[row][j] == 1 and (row,j) not in visited:
                        bucket_count += 1
                        visited.add((row,j))
                        if bucket_count == capacity:
                            return bucket_count
                            break
                        elif (row + 1,j) not in rows_to_fill
