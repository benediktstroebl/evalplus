
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
    # n = len(grid)
    # m = len(grid[0])
    # min_lst = []
    # before = 0
    # after = 1
    # if n == 1 and m == 1:
    #     return [grid[0][0]]
    # min_lst.append(grid[0][0])
    # if n == 1:
    #     return min_lst
    # elif m == 1:
    #     return grid[0]
    # while after < n:
    #     min_lst.append(grid[before][after])
    #     before += 1
    #     after += 1
    #     if n - after < before:
    #         after -= 1
    #         before -= 1
    # return min_lst

    # better use graph
    m = len(grid[0])
    if m == 1:
        return grid[0]
    graph = [[] for _ in xrange(m)]
    min_lst = grid[0]
    visited = set()
    for i in xrange(1, m):
        if grid[0][i] < min_lst[0]:
            min_lst[0] = grid[0][i]
    visited.add(grid[0][0])
    node = [grid[0][0]]
    i = 0
    # Go through the first line and add all edges to graph
    for j in xrange(1, m):
        if grid[0][j] > min_lst[i]:
            min_lst[i + 1] = grid[0][j]
            node.append(grid[0][j])
            visited.add(grid[0][j])
            graph[j].append(0)
            i += 1
    for i in xrange(1, k):
        for j in xrange(m):
            if graph[j] == []:
                continue
            if grid[i][j] not in visited:
                visited.add(grid[i][j])
                min_lst[i + 1] = grid[i][j]
                node.append(grid[i