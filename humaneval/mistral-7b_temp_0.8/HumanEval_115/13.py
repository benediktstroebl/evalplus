
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

    def travel_with_bucket(grid, capacity, current_x, current_y, n, m, visited):
        current_state = grid[current_x][current_y]
        if current_state == 0:
            return False

        for i, j in [(current_x + 1, current_y), (current_x - 1, current_y), (current_x, current_y + 1), (current_x, current_y - 1)]:
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if grid[i][j] != 0:
                return False

        if visited[current_x][current_y]:
            return False
        visited[current_x][current_y] = True

        if current_state < capacity:
            grid[current_x][current_y] = 0
            visited[current_x][current_y] = True
            for i, j in [(current_x + 1, current_y), (current_x - 
