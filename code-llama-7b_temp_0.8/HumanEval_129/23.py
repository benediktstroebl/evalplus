
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
    #############
    # Brute Force
    #############
    # # Find all possible path
    # allPaths = []
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         path = []
    #         dfs(i, j, path, grid, set([]), k)
    #         if len(path) == k:
    #             allPaths.append(path)

    # # Find the min path
    # minPath = allPaths[0]
    # for i in range(len(allPaths)):
    #     if compare(allPaths[i], minPath):
    #         minPath = allPaths[i]

    # return minPath

    # def compare(lst1, lst2):
    #     if len(lst1) != len(lst2):
    #         return False
    #     for i in range(len(lst1)):
    #         if lst1[i] < lst2[i]:
    #             return False
    #     return True

    # def dfs(i, j, path, grid, visited, k):
    #     if k == 0:
    #         return
    #     visited.add((i,j))
    #     path.append(grid[i][j])
    #     for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
    #         if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[i]):
    #             if (x, y) not in visited:
    #                 dfs(x, y, path, grid, visited, k-1)
    #     visited.remove((i, j))
    #     path.pop()

    #############
    # Dynamic Programming
    #############
    n, m = len(grid), len(grid[0])
    # Create a 2-d matrix to store the minimum length of path ending at a particular cell
    # dp[i][j] = minimum length
