
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
    import math

    def fill(grid, i, j, bucket_capacity, buckets, target, visited):
        if target < 0:
            return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        if grid[i][j] == 0 or i in visited:
            return

        if grid[i][j] == 1:
            bucket_capacity += 1
            if bucket_capacity >= target:
                return

        visited.append(i)
        fill(grid, i-1, j, bucket_capacity, buckets, target, visited)
        fill(grid, i+1, j, bucket_capacity, buckets, target, visited)
        fill(grid, i, j-1, bucket_capacity, buckets, target, visited)
        fill(grid, i, j+1, bucket_capacity, buckets, target, visited)
        visited.pop()
        if bucket_capacity >= target:
            buckets += 1
            target = math.inf
        else:
            buckets = buckets
        return buckets

    buckets = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            target = sum(grid[i])
            buckets = max(fill(grid, i, j, 0, buckets, target, []), buckets)

    return buckets

