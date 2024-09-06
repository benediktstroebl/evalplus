
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

    def solution(grid, capacity):
        """
        :type grid: List[List[int]]
        :type capacity: int
        :rtype: int
        """
        import math
        # Calculate water
        height = len(grid)
        width = len(grid[0])
        filled = 0
        for y in range(height):
            for x in range(width):
                filled += grid[y][x]
        # Solve equation
        target = filled - capacity
        count = 0
        if target > 0:
            # Find max contiguous filled
            max_contiguous = 0
            for y in range(height):
                for x in range(width):
                    contiguous = grid[y][x]
                    if contiguous == 1:
                        for j in range(x+1, width):
                            if grid[y][j] == 0:
                                break
                            else:
                                contiguous += 1
                        for i in range(y+1, height):
                            if grid[i][x] == 0:
                                break
                            else:
                                contiguous += 1
                    max_contiguous = max(max_contiguous, contiguous)
            count = math.ceil(target/max_contiguous)
        return count

    return solution


