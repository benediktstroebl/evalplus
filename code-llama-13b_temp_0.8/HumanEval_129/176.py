
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

    def getNeighbors(grid, i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j))
        if i < len(grid) - 1:
            neighbors.append((i+1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if j < len(grid[i]) - 1:
            neighbors.append((i, j+1))
        return neighbors

    if not grid or not grid[0]:
        return None

    n = len(grid)
    m = len(grid[0])

    # track the previous node
    parent = [[None]*m for _ in range(n)]

    # track the step from starting node
    step = [[float('inf')]*m for _ in range(n)]

    # visited nodes
    visited = set()

    # queue to store the next nodes
    q = []

    # starting node is (0, 0)
    q.append((0, 0, 0))

    # starting node has no parent
    parent[0][0] = None

    # starting node has no step
    step[0][0] = 0

    while q:
        # pop the first node from the queue
        i, j, s = q.pop(0)

        # check if the node is visited
        if (i, j) in visited:
            continue

        # add the node to the visited set
        visited.add((i, j))

        # check if the node is the destination
        if s == k:
            break

        # for the current node, explore all the neighbors
        for ni, nj in getNeighbors(grid, i, j):
            if (ni, nj) not in visited:
                # add the neighbor to the queue
                q.append((ni, nj, s+1))
                # update the parent
                parent[ni][nj] = (i, j)
                # update the step
                step[ni][nj] = s + 1

    # starting node
