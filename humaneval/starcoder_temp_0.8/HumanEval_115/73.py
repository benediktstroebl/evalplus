
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
    # Time complexity: O(r*c), where r is the number of rows in the grid,
    # and c is the number of columns in the grid.
    # Space complexity: O(r*c).
    # This is because the depth of the recursion stack can grow up to r*c.
    def helper(grid, capacity, row, col, count):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return count

        if grid[row][col] == 1:
            grid[row][col] = 0
            count = helper(grid, capacity, row - 1, col, count)
            count = helper(grid, capacity, row + 1, col, count)
            count = helper(grid, capacity, row, col - 1, count)
            count = helper(grid, capacity, row, col + 1, count)
        elif grid[row][col] == 0 and count < capacity:
            count += 1
            grid[row][col] = 1

        return count

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count = helper(grid, capacity, i, j, count)

    return count
