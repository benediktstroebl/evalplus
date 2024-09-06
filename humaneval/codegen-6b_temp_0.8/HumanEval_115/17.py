
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
    
    # Least number of buckets you need to empty all the wells
    # Use BFS to check the number of times we need to empty a well
    # Use another BFS to check the number of times we need to empty a well
    # grid[i][j] -> 0 for empty, 1 for full
    # bucket's capacity is 1
    # bucket_capacity is a global variable
    # Use a priority queue to know which bucket to choose
    # We store the full well capacity (number of 1) in a tuple, (well_id, bucket_id, well_capacity)
    # We also store the empty well id in well_id
    # We also store the bucket id in bucket_id
    # BFS to find all the empty wells

    # visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # bucket_capacity = bucket_capacity
    # w_id = 0
    # b_id = 0
    # wells = []
    # q = [(0, 0, 0)]
    # while q:
    #     i, j, well_capacity = q.pop(0)
    #     wells.append((w_id, b_id, well_capacity))
    #     visited[i][j] = True
    #     if well_capacity == 0:
    #         b_id += 1
    #         q.append((i, j, 0))
    #     else:
    #         q.append((i-1, j, well_capacity-1))
    #         q.append((i+1, j, well_capacity-1))
    #         q.append((i, j-1, well_capacity-1))
    #         q.append((i, j+1, well_capacity-1))
    # wells.sort()
    # for w_id, b_id, well_capacity in wells:
    #     bucket = []
    #     min_b_id = b_id
    #     while bucket_capacity > 0 and well_capacity > 0:
    #         bucket.append(w_id)
    #         well_capacity = well_capacity - bucket_