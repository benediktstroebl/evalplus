
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
    def fill_left(grid, y, capacity):
        """
        Fill as much as possible from the left
        """
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                continue
            for i in range(x+1):
                if i+capacity > len(grid[y]):
                    continue
                if sum(grid[y][x:x+capacity]) != capacity:
                    continue
                grid[y] = [1 if x == 1 else 0 for x in grid[y]]
                for i in range(x, x+capacity):
                    grid[y][i] = 1
                return True
        return False

    def fill_right(grid, y, capacity):
        """
        Fill as much as possible from the right
        """
        for x in range(len(grid[y])):
            if grid[y][-x-1] == 1:
                continue
            for i in range(x+1):
                if i+capacity > len(grid[y]):
                    continue
                if sum(grid[y][-capacity-x:-x]) != capacity:
                    continue
                grid[y] = [1 if x == 1 else 0 for x in grid[y]]
                for i in range(-x-capacity, -x):
                    grid[y][i] = 1
                return True
        return False

    def fill_top(grid, x, capacity):
        """
        Fill as much as possible from the top
        """
        for y in range(len(grid)):
            if grid[y][x] == 1:
                continue
            for i in range(y+1):
                if i+capacity > len(grid):
                    continue
                if sum([row[x] for row in grid[y:y+capacity]]) != capacity:
                    continue
                for row in grid[:y+capacity]:
                    row[x] = 1
                return True
        return False

    def fill_bottom(grid, x, capacity):
        """
        Fill as
