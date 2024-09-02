
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
    # 1. For each row find the first bucket which can be filled.
    # 2. For that bucket, find the highest bucket it can fill.
    # 3. Fill from highest to lowest.
    # 4. Repeat 1-3 until no more can be filled.
    # 5. If more buckets can be filled, return "impossible"
    filled = [[0] * len(row) for row in grid]
    cur_height = 0
    while True:
        # 1.
        can_fill = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if filled[r][c]:
                    continue
                if grid[r][c]:
                    can_fill.append((r, c))
        # 2.
        buckets = []
        for r, c in can_fill:
            height = 1
            for i in range(r + 1, len(grid)):
                if filled[i][c]:
                    break
                if grid[i][c]:
                    height += 1
                else:
                    break
            buckets.append((r, c, height))
        # 3.
        if not buckets:
            break
        # 4.
        bucket_count = math.ceil(capacity / sum([b[2] for b in buckets]))
        for _, c, _ in buckets:
            filled[cur_height][c] = 1
        for _ in range(bucket_count):
            if cur_height < len(grid) - 1:
                cur_height += 1
            else:
                break
    return sum(sum(row) for row in filled)

