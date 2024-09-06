
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

    visited = set()
    queue = []
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and not (i,j) in visited:
                queue.append((i,j))
                visited.add((i,j))
                while queue:
                    x, y = queue.pop()
                    for k in range(4):
                        if x+k-1 >= 0 and y+k-1 >= 0 and x+k-1 < len(grid) and y+k-1 < len(grid[0]) and grid[x+k-1][y+k-1] == 1 and (x+k-1,y+k-1) not in visited:
                            queue.append((x+k-1,y+k-1))
                            visited.add((x+k-1,y+k-1))
                count += 1
    return count

