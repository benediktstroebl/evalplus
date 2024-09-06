
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
    def neighbours(r, c):
        """
        Produces the neighbours of the cell (r, c)
        """
        for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
            if 0 <= nr < N and 0 <= nc < N:
                yield nr, nc

    N = len(grid)
    if N == 0 or k == 0 or grid is None or grid[0] is None:
        return []

    dist = [[float('inf')] * N for _ in range(2)]

    stack = [(0, 0)]
    dist[0][0] = grid[0][0]
    dist[1][0] = float('inf')

    while stack:
        r, c = stack.pop()
        for nr, nc in neighbours(r, c):
            if 0 <= nr < N and 0 <= nc < N and dist[0][nr] > dist[0][c] + grid[nr][nc]:
                dist[0][nr] = dist[0][c] + grid[nr][nc]
                dist[1][nr] = min(dist[1][nr], dist[1][c] + 1)
                stack.append((nr, nc))

    result = []
    for i in range(k):
        if dist[0][i] != float('inf') and dist[1][i] != float('inf'):
            result.append(dist[0][i])
    return result


assert minPath([[1,2,3], [4,5,6], [7,8,9]], 3) == [1, 2, 1]
assert minPath([[5,9,3], [4,1,6], [7,8,2]], 1) == [1]
