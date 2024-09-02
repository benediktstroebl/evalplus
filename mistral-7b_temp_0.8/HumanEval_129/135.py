
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
    def recursive(grid, visited, k, x, y, current_path, min_path):
        if k == 0:
            visited[x][y] = 1
            min_path.append(current_path.pop())
            visited[x][y] = 0
            return 1
        min_len = 100000
        for dir in range(4):
            i = x + dir - 2
            j = y + dir - 2
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if not visited[i][j]:
                    current_path.append(grid[i][j])
                    visited[i][j] = 1
                    l = recursive(grid, visited, k - 1, i, j, current_path, min_path)
                    visited[i][j] = 0
                    if l == 1:
                        min_len = min(min_len, len(current_path))
                        min_path.append(current
