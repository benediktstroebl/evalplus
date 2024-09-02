
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
    # all wells have the same length
    # initialize filled wells
    filled = set()
    # get filled wells
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                filled.add((i,j))
    # print(filled)
    # traverse all buckets
    # 1. find all connected buckets
    # 2. calculate the max filled wells
    # 3. traverse connected buckets
    def bfs(bucket_position):
        visited = set()
        q = []
        q.append(bucket_position)
        visited.add(bucket_position)
        # print("q:", q)
        while len(q) > 0:
            i, j = q.pop(0)
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_i, new_j = i + di, j + dj
                if new_i >= 0 and new_j >= 0 and new_i < r and new_j < c and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                    q.append((new_i, new_j))
                    visited.add((new_i, new_j))
        return visited
    
    # get all connected buckets
    def find_connected_buckets(grid, r, c, filled):
        connected_buckets = []
        for i in range(r):
            for j in range(c):
                # if (i,j) not in filled:
                if grid[i][j] == 1:
                    bucket = bfs((i,j))
                    # print("bucket:", bucket)
                    connected_buckets.append(bucket)
        return connected_buckets

    # calculate the max filled wells
    def max_filled(connected_buckets):
        filled_wells = []
        for bucket in connected_buckets:
            filled_wells.append(len(bucket))
        # print("filled_wells:", filled_wells)
        return max(filled_wells)

    # calculate the capacity
    capacity = math.ceil(capacity/2)
    # print("capacity:", capacity)

    connected_buckets = find_connected_buckets
