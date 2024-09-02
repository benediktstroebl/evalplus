
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
    def dfs(grid, cell, path, k):
        """
        DFS (depth-first search) is used to find the minimum path.
        """
        if cell == (k, k): # return immediately if path is k long
            return path + [grid[cell]]

        for i in range(4):
            for j in range(4):
                if (cell == (i, j)) or (cell == (i, j+1) or cell == (i+1, j)):
                    # visit neighbors
                    grid_index = (i, j)
                    if not path or (path[-1] == grid[grid_index[0]] and path[-1] == grid[grid_index[1]]):
                        path.append(grid[grid_index[0]][1])
                    else:
                        path.append(path[-1])

        # update path
        path.append(grid[cell])
        cell = (0, 0) # do not return to the starting cell

        return path[-1] # get the last element of the path

    def dfs_helper(grid, i, j, k):
        """
        DFS helper function.
        """
        if (i, j) in grid: # return immediately if cell is not empty
            return grid[i][j]

        if (i, j) in path: # return previously visited cells
            return path[path.index((i, j))]

        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])) or (i < 1 or j < 1 or i >= len(grid) or j >= len(grid[0])):
            return None # invalid cell

        if (i, j) == (k-1, k-1): # return the cell in the bottom right corner
            return grid[k-1][k-1]

        if (i, j) == (0, 0): # return the cell in the top left corner
            return grid[0][0]

        path.append((i, j)) # add the current cell to path
        dfs_helper(grid, i+
