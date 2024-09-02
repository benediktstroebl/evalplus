
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
    from collections import deque
    from heapq import heappush, heappop

    def get_directions():
        for d in (1, -1), (1, 0), (0, 1):
            yield d

    def get_neighbors(r, c):
        for dx, dy in get_directions():
            if 0 <= r+dx < len(grid) and 0 <= c+dy < len(grid[0]):
                yield r+dx, c+dy

    def minimum_path(r, c):
        q = [(0, [grid[r][c]])]
        visited = set()
        while q:
            cost, path = heappop(q)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if len(path) == k:
                return path
            for rr, cc in get_neighbors(r, c):
                heappush(q, (cost+grid[rr][cc], path+[grid[rr][cc]]))

    return minimum_path(0, 0)

