
def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with you current
    cell.
    Please note that a path of length k means visiting exactly k cells (not
    necessarily distinct).
    You CANNOT go off the grid.
    A path A (of length k) is considered less than a path B (of length k) if
    after making the ordered lists of the values on the cells that A and B go
    through (let's call them lst_A and lst_B), lst_A is lexicographically less
    than lst_B, in other words, there exist an integer index i (1 <= i <= k)
    such that lst_A[i] < lst_B[i] and for any j (1 <= j < i) we have
    lst_A[j] = lst_B[j].
    It is guaranteed that the answer is unique.
    Return an ordered list of the values on the cells that the minimum path go through.

    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    grid = [row[:] for row in grid]
    
    # initialization
    for i in range(len(grid)):
        row = grid[i]
        if 1 in row:
            row[row.index(1)] = i + 1
            for j in range(len(row)):
                if row[j] == i + 1:
                    row[j] = 0
        else:
            row[row.index(1)] = 1
            
    def recursive_helper(grid, row, col, k, lst):
        if row == len(grid) or col == len(grid[0]):
            return None
        
        if k == 1:
            lst.append(grid[row][col])
            return None
        
        if k - 1 > 0 and grid[row][col] >= grid[row + 1][col]:
            lst.append(grid[row][col])
            return recursive_helper(grid, row + 1, col, k - 1, lst)
        else:
            lst.append(grid[row][col])
            return recursive_helper(grid, row, col + 1, k - 1, lst)
        
    
    def helper(grid, row, col, k):
        if row == len(grid) or col == len(grid[0]):
            return None
        
        if k == 1:
            lst = [l for l in grid[row][col:]]
            grid[row][col:] = lst[-k:]
            return lst
        
        min_path = min(helper(grid, row + 1, col, k - 1), helper(grid, row, col + 1, k - 1))
        if min_path is not None:
            lst = [l for l in min_path]
            grid[row][col:] = lst[-k:]
            return lst
        
        else:
            lst = [l for l in grid[row][col:]]
            grid[row][col:] = lst[-k:]
            return lst
        
    path = helper(grid, 0, 0, k)
    
    return