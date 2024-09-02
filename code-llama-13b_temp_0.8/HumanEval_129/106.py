
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
    """
    :param grid: List[List[int]]
    :param k: int
    :return: List[int]
    """
    #n = len(grid)
    # if grid is empty
    if len(grid) == 0:
        return []
    # if grid is square
    if len(grid) == len(grid[0]):
        # if grid is 1 row
        if len(grid) == 1:
            if k >= len(grid[0]):
                return grid[0]
            else:
                return []
        # if grid is 2 rows
        if len(grid) == 2:
            if k >= len(grid[0]):
                return grid[0] + grid[1]
            else:
                return []
        # otherwise grid is N rows
        else:
            for i in range(len(grid) - 1):
                if i == 0:
                    grid[i].append(grid[i][len(grid[i]) - 1] + grid[i + 1][0])
                else:
                    grid[i].append(grid[i][len(grid[i]) - 1] + grid[i + 1][0])
                for j in range(len(grid[i]) - 2, 0, -1):
                    grid[i][j] += grid[i][j + 1]
            if k >= len(grid[len(grid) - 1]):
                return grid[0] + grid[len(grid) - 1]
            else:
                return []
    # otherwise grid is not square
    else:
        return []
