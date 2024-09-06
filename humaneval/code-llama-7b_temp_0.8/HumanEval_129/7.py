
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

    # create a queue
    queue = deque()
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]

    # add the first cell to the queue
    queue.append((0, 0))

    # BFS
    while queue:
        # pop the first element of the queue
        x, y = queue.popleft()

        # check if the current position has already been visited
        if visited[x][y]:
            continue

        # add it to the visited list
        visited[x][y] = True

        # if the current position is the last cell, we have found the shortest path
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            return grid[x][y]

        # add neighbors to the queue, except for those which have already been visited
        if x - 1 >= 0 and not visited[x - 1][y]:
            queue.append((x - 1, y))
        if x + 1 < len(grid) and not visited[x + 1][y]:
            queue.append((x + 1, y))
        if y - 1 >= 0 and not visited[x][y - 1]:
            queue.append((x, y - 1))
        if y + 1 < len(grid[0]) and not visited[x][y + 1]:
            queue.append((x, y + 1))

