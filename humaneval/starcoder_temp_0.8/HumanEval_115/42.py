
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
    if not grid:
        return 0

    grid_length = len(grid)
    grid_width = len(grid[0])

    # maintain a queue
    # [x, y, water_remaining]
    queue = deque()
    for i in range(grid_length):
        for j in range(grid_width):
            if grid[i][j] == 1:
                queue.append([i, j, capacity])

    # for each bucket, find its bottom right boundary
    buckets = []
    for i in range(grid_length):
        for j in range(grid_width):
            if grid[i][j] == 0:
                top = i + 1
                bottom = i - 1
                left = j + 1
                right = j - 1

                while top < grid_length and grid[top][j] == 1:
                    top += 1
                while bottom >= 0 and grid[bottom][j] == 1:
                    bottom -= 1
                while left < grid_width and grid[i][left] == 1:
                    left += 1
                while right >= 0 and grid[i][right] == 1:
                    right -= 1
                # for each bucket, add to queue
                buckets.append([top, bottom, left, right])
    print(buckets)

    # get the fill order by BFS
    # fill buckets first
    # then fill the rest of the water
    # fill the rest of the water first to avoid overflow
    # stop when no more fills
    fill_order = []
    while queue or buckets:
        # fill the buckets first
        while buckets and queue:
            top, bottom, left, right = buckets.pop()
            # check if it can be filled
            if top - bottom < capacity and left - right < capacity:
                fill_order.append([top, bottom, left, right])
                for i in range(top, bottom - 1, -1):
                    grid[i][left] = 0
                    grid[i][right] = 0
                for j in range(left, right - 1, -1):
                    grid[top][j] = 0
                    grid[bottom][j] = 0
            else:
                buckets.append([top, bottom, left, right])
        if not buckets:
            # fill the rest of the water
            for i in range(grid_length
