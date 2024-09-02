
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
    N = len(grid)
    if N < 2:
        raise ValueError

    if k == 0:
        return None
    if k == 1:
        return [i[0] for i in grid]

    if k == 2:
        g = [['%s' % i[0], i[1], i[2]] for i in grid]
        return [1, 1, 1] if sorted(g) == g else [1, 1, 1]

    visited = [[False] * N for i in range(N)]
    queue = []
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            queue.append([[i, j], [grid[i][j]], 1])
            visited[i][j] = True
    visited = [[False] * N for i in range(N)]

    while queue:
        current = queue.pop(0)
        i, j = current[0][0], current[0][1]
        visited[i][j] = True
        if len(current[1]) == k:
            break
        if current[2] < k:
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < N and 0 <= y < N and not visited[x][y]:
                    new_values = [1 if current[1][0] < current[1][1] else 2] + current[1]
                    new_queue = [[[x, y], new_values, current[2] + 1]]
                    while new_queue:
                        new_current = new_queue.pop(0)
                        nx, ny = new_current[0][0], new_current[0][1]
                        if new_current[2] < k:
                            visited[nx][ny] = True
                            new_queue.append([[nx + 1, ny], new_current[1][:], new_current[2] + 1])
                            new_queue.append([[nx - 1, ny], new_