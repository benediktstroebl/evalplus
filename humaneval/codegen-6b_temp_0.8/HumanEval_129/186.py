
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
    m = len(grid)
    n = len(grid[0])

    def grid_to_set(i, j):
        return set(grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j]+grid[i+1][j+1]+grid[i+1][j+2]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2])

    # Returns the k-th smallest integer in grid[0][0] through grid[m-1][n-1]
    def kthSmallest(grid, m, n, k):
        if m == 1 and n == 1 and k == 1:
            return grid[0][0]

        visited = set()
        visited.add(tuple(grid[0][0:3]))
        visited.add(tuple(grid[0][3:6]))
        visited.add(tuple(grid[0][6:9]))
        visited.add(tuple(grid[1][0:1]))
        visited.add(tuple(grid[1][1:2]))
        visited.add(tuple(grid[1][2:3]))
        visited.add(tuple(grid[2][0:1]))
        visited.add(tuple(grid[2][1:2]))
        visited.add(tuple(grid[2][2:3]))

        all_sums = []

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if tuple(grid[i][j:j+3]) not in visited:
                    visited.add(tuple(grid[i][j:j+3]))
                    all_sums.append([grid[i][j], grid[i][j+1], grid[i][j+2]])
                if tuple(grid[i][j:j+1] + grid[i][j+1] + grid[i][j+2]) not in visited:
                    visited