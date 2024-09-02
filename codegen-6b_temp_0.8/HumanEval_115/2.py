
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
    
    # first find the max rectangular area for each row
    length = len(grid)
    width = len(grid[0])
    square = [[0]*(width+1) for _ in range(length+1)]
    def max_area(row, col):
        if row == length and col == width: return 0
        return max(square[row][col], square[row][col+1] - 1, square[row+1][col] - 1, square[row+1][col+1] - (1 if col == width-1 else 0))
        
    # fill the grid in the area
    for i in range(length):
        for j in range(width):
            square[i+1][j+1] = square[i][j+1] + 1 if grid[i][j] == 1 else square[i+1][j] + 1
        square[i+1][0] -= 1
    result = max_area(0, 0)
    
    for row in square:
        print(row)
    print("-----------------------------")
    
    # lower the buckets
    for col in range(width):
        # find the first 0
        for row in range(length):
            if grid[row][col] == 0:
                break
            if row == length-1:
                result += 1
                continue
        
        # keep track of the last column
        last_col = col
        for row in range(length):
            if grid[row][col] == 0 and grid[row][last_col]:
                result -= 1
            elif grid[row][col]:
                last_col = col
    return result

assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 2) == 5
assert max_fill([[0,0,0], [0,0,0]], 5) == 0
assert max_fill([[0]], 5) == 0
assert max_fill([[0