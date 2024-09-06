
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
    import heapq
    heap = []
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c > 0:
                heapq.heappush(heap, (c, i, j, 0))
    width = len(grid[0])
    heap = sorted(heap, key=lambda x: x[0] / math.sqrt(width ** 2 + width))
    count = 0
    while heap and capacity >= 0:
        c, x, y = heap[0]
        if capacity - c >= 0:
            capacity -= c
            count += 1
        heapq.heappop(heap)
        if grid[x][y] > 0:
            heapq.heappush(heap, (grid[x][y], x, y, 0))
    return count

