
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
    # get all possible unique cells
    rc = len(grid)
    cc = len(grid[0])

    # initially, we have no path because we have to choose one
    path = []

    # we use a dictionary to record the visited status
    # in the above example, we have to finish at [1, 2, 1]
    visited = {}

    # we can choose any cell as starting point
    for r in range(rc):
        for c in range(cc):
            # if we visit this cell before, we don't need to visit it again
            if (r, c) in visited:
                continue

            # add this cell to the path
            path.append(grid[r][c])

            # if the path length is larger than k, we can no longer add to the path
            # so we need to backtrack to the previous cell
            if len(path) >= k:
                path.pop()
                visited[(r, c)] = False

            # this is the new path
            new_path = []

            # we can go to neighboring cells with the same edge
            # if the neighbor is visited before, we can still find a shorter
            # path for this neighbor
            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < rc and 0 <= nc < cc:
                    if (nr, nc) in visited:
                        new_path.append(grid[nr][nc])

            # since we only allow to visit unique cells, we can iteratively
            # remove the shorter path
            for i in range(1, len(new_path)):
                if new_path[i - 1] < new_path[i]:
                    new_path.pop(i - 1)
                    break

            # add the new path to the path
            path += new_path

            # since we don't want to visit same cell again, we mark it as visited
            visited[(r, c)] = True

    return path

