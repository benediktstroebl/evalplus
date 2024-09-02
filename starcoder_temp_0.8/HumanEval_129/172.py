
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
    # #Method 1
    # def dfs(grid, i, j, k, visited):
    #     if k == 0:
    #         return True
    #     if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] < 1 or grid[i][j] > 9 or (i,j) in visited:
    #         return False
    #     visited.add((i,j))
    #     for row, col in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
    #         if dfs(grid, row, col, k-1, visited):
    #             return True
    #     return False
    #
    # min_path = [float("inf")] * 9
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if dfs(grid, i, j, k, set()):
    #             min_path[grid[i][j]-1] = min(min_path[grid[i][j]-1], abs(i-j))
    #
    # return [i+1 for i, val in enumerate(min_path) if val == min(min_path)]


    # #Method 2
    # def dfs(grid, i, j, k, visited):
    #     if k == 0:
    #         return True
    #     if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] < 1 or grid[i][j] > 9 or (i,j) in visited:
    #         return False
    #     visited.add((i,j))
    #     min_val = float("inf")
    #     for row, col in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
    #         if dfs(grid, row, col, k-1, visited):
    #             min_val = min(min_val, abs(i-j))
    #     return min_val
    #
    # min_path = [float("inf")] * 9
    # for i in range(len(grid
