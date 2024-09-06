
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
    if k == 1:
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res.append(grid[i][j])
                    break
        return res
    # print(grid)
    col = len(grid[0])
    visited = [False for _ in range(col)]
    visited[0] = True
    res = [1]
    for i in range(col):
        res.append(grid[0][i])
    for i in range(1, col):
        visited[i] = True
        for j in range(i):
            if grid[i][j] < grid[i][i - 1]:
                res[i] = grid[i][j]
                visited[j] = True
                break
    for i in range(1, len(grid)):
        if k - len(res) <= 0:
            break
        visited[0] = True
        if grid[i][0] < res[0]:
            res[0] = grid[i][0]
            visited[0] = True
        for j in range(1, col):
            if not visited[j]:
                if grid[i][j] < res[j]:
                    res[j] = grid[i][j]
                elif grid[i][j] == res[j]:
                    res[j] = grid[i][j]
                    visited[j] = True
        for j in range(1, col):
            if not visited[j]:
                if grid[i][j] <= res[j - 1]:
                    res[j] = grid[i][j]
                elif grid[i][j] > res[j - 1]:
                    for k in range(j - 1):
                        if grid[i][k] <= res[k]:
                            res[k + 1] = grid[i][j]
                            break
                    res[j] = grid[i][j]
    return res

