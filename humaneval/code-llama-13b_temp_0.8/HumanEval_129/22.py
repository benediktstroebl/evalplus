
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
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return None

    N = len(grid)
    M = len(grid[0])

    if N * M < k:
        return None
    
    def get_min_path(grid, k, r, c):
        N = len(grid)
        M = len(grid[0])

        memo = [[-1] * (M + 1) for _ in range(N + 1)]

        memo[r][c] = 0

        queue = [(r, c)]

        while queue:
            r, c = queue.pop(0)
            for nr, nc in [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]:
                if 0 <= nr < N and 0 <= nc < M and memo[nr][nc] == -1:
                    memo[nr][nc] = memo[r][c] + 1
                    if memo[nr][nc] == k:
                        return grid[nr][nc]
                    queue.append((nr, nc))
        
        return None
    
    min_value = grid[0][0]
    r, c = 0, 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] < min_value:
                min_value = grid[i][j]
                r, c = i, j
    
    kth_value = grid[r][c]

    path = [min_value]

    while True:
        value = get_min_path(grid, k, r, c)
        if value is None:
            return None
        if value == kth_value:
            return path
        path.append(value)
        k -= 1

    
