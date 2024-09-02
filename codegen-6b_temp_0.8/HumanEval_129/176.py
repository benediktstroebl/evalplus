
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
    grid = list(map(list, grid))
    m = len(grid)
    n = len(grid[0])

    # use BFS to find the destination
    queue = collections.deque()
    # distance to destination
    dist = collections.defaultdict(int)
    # distance to source
    dist[(0, 0)] = grid[0][0]
    # can NOT be travelled to
    can_not_go = {}
    # the next destination, (row, col)
    destination = {}

    # find the destination, and mark as not visited
    for row in range(m):
        for col in range(n):
            if grid[row][col] == k + 1:
                # find the destination
                destination[(row, col)] = (row, col)
                queue.append((row, col))

    while len(queue):
        row, col = queue.popleft()
        # can_not_go[(row, col)] = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                # can not go to destination
                if i == 0 and j == 1:
                    can_not_go[(row, col)] = True
                # can not go down
                if i == 1 and j == 0:
                    can_not_go[(row, col)] = True
                # can not go right
                if i == 0 and j == -1:
                    can_not_go[(row, col)] = True
                # can not go up
                if i == -1 and j == 0:
                    can_not_go[(row, col)] = True
                # can not go left
                if i == 0 and j == 1:
                    can_not_go[(row, col)] = True
                # can not go left
                if i == 1 and j == 1:
                    can_not_go[(row, col)] = True

                # not visited
                if (row, col) not in can_not_go:
                    # can go to destination
                    if (row, col) in destination:
                        queue