
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
    # Inefficient.
    # Don't see how to get it to work efficiently.
    # Brute force DFS doesn't scale.
    # You have to be able to backtrack from anywhere.
    # Need to be able to keep track of where you've already been.
    # Come back to a cell and continue where you left off.
    # Immediately reject if you start on the wrong track.
    # If you go off track, you have to backtrack.
    # If you backtrack, you have to keep track of where you've been and what
    # choices you've made.

    # Brute force:
    # O(n!), O(n)
    # def get_paths(grid, visited, i, j, k):
    #     if k < 0:
    #         return
    #     # get all valid neighbors
    #     for (di, dj) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
    #         newi, newj = i + di, j + dj
    #         if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and (newi, newj) not in visited:
    #             visited.add((newi, newj))
    #             get_paths(grid, visited, newi, newj, k - 1)

    # grid = tuple(tuple(r) for r in grid)
    # for (i, j) in product(range(len(grid)), repeat=2):
    #     visited = {(i, j)}
    #     get_paths(grid, visited, i, j, k)

    # print("Visited:", visited)

    # paths = []
    # for (i, j) in visited:
    #     path = grid[i][j:j + k]
    #     paths.append(tuple(path))

    # if not paths:
    #     return None

    # return sorted(paths)[0]

    # Optimized DFS
    # Keep track of each path in a list, and maintain
