
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
    def extract_water(grid, bucket_capacity):
        rows = len(grid)
        cols = len(grid[0])

        rows_to_visit = [0 for _ in range(rows)]
        cols_to_visit = [True for _ in range(cols)]
        current_bucket_capacity = 0
        visited_wells = 0

        while sum(rows_to_visit) < rows:
            visited_wells += 1

            # visit a row
            for i in range(rows-1, -1, -1):
                if rows_to_visit[i] == 0:
                    continue

                for j in range(cols):
                    if grid[i][j] == 1:
                        if cols_to_visit[j] == True:
                            current_bucket_capacity += 1
                        if current_bucket_capacity == bucket_capacity:
                            rows_to_visit[i] = 0
                            cols_to_visit[j] = False
                            break
                if rows_to_visit[i] == 0:
                    break

        return visited_wells

    def check(grid, bucket_capacity):
        if not grid or not grid[0]:
            return 0

        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return extract_water(grid, bucket_capacity)
        return 0

    bucket_capacity = math.floor(bucket_capacity / (1.0 * sum([sum(r) for r in grid])))
    return check(grid, bucket_capacity)

