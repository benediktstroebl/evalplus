
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
    def get_min(row, bucket_capacity):
        """
        O(n)
        """
        cnt = 0
        for i in row:
            if i > 0:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
        return bucket_capacity - cnt

    def max_fill_util(i, j, grid, bucket_capacity, visited):
        """
        O(n)
        """
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        if visited[i][j]:
            return 0
        visited[i][j] = True
        min_ = get_min(grid[i], bucket_capacity)
        if min_ == 0:
            return 0

        max_ = 0
        max_ += max_fill_util(i-1, j, grid, bucket_capacity, visited)
        max_ += max_fill_util(i+1, j, grid, bucket_capacity, visited)
        max_ += max_fill_util(i, j-1, grid, bucket_capacity, visited)
        max_ += max_fill_util(i, j+1, grid, bucket_capacity, visited)

        if grid[i][j] > min_:
            max_ += math.ceil(grid[i][j] / min_)
        return max_
    
    visited = []
    for _ in grid:
        visited.append([False for _ in _])
    return max_fill_util(len(grid)-1, len(grid[0])-1, grid, bucket_capacity, visited)
