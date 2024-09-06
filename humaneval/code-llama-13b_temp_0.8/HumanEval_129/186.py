
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
    if k > (grid[0][0] + grid[1][1] + grid[2][2]) / 3:
        return []
    visited = [[0] * len(grid[0]) for _ in grid]
    min_path = grid[0][0]
    min_idx = [0, 0]
    def dfs(y, x, path):
        if path >= k:
            return
        if visited[y][x] == 0:
            visited[y][x] = 1
            for i, j in [[y+1, x], [y-1, x], [y, x+1], [y, x-1]]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    if grid[i][j] < min_path:
                        min_path = grid[i][j]
                        min_idx = [i, j]
                    if not visited[i][j]:
                        dfs(i, j, path+1)
                        visited[i][j] = 0
    dfs(0, 0, 0)
    result = []
    while min_path != 0:
        result.append(min_path)
        visited[min_idx[0]][min_idx[1]] = 0
        min_path = 0
        for i, j in [[min_idx[0]-1, min_idx[1]], [min_idx[0]+1, min_idx[1]], [min_idx[0], min_idx[1]-1], [min_idx[0], min_idx[1]+1]]:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                if grid[i][j] < min_path:
                    min_path = grid[i][j]
                    min_idx = [i, j]
        if min_path == 0:
            break
    return result
