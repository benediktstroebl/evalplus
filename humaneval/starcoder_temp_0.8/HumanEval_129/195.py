
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
    n = len(grid)
    q = deque()
    q.append((0, 0))
    while k > 0:
        sz = len(q)
        for _ in range(sz):
            r, c = q.popleft()
            if r == n - 1 and c == n - 1:
                k -= 1
            else:
                for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                    if 0 <= nr < n and 0 <= nc < n:
                        q.append((nr, nc))

    def _dfs(grid, i, j, k, visited, out):
        if i == j == n - 1:
            out.append(grid[i][j])
            return
        visited[i][j] = True
        for nr, nc in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                _dfs(grid, nr, nc, k, visited, out)
        visited[i][j] = False

    visited = [[False for _ in range(n)] for _ in range(n)]
    out = []
    _dfs(grid, 0, 0, k, visited, out)
    return out
