
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
    if len(grid) < 2:
        return grid

    for row in grid:
        row.insert(0, None)

    for row in range(1, len(grid)):
        grid[row].insert(0, None)

    for row in range(1, len(grid)):
        grid[row][0] = grid[row - 1][0] + grid[row][0]

    for column in range(1, len(grid[0])):
        grid[0][column] = grid[0][column - 1] + grid[0][column]

    for row in range(1, len(grid)):
        for column in range(1, len(grid[0])):
            grid[row][column] = grid[row - 1][column] + grid[row][column]

    total = 0
    for i in range(k):
        total += grid[i][0] + grid[i][-1]

    # n = len(grid)
    # m = len(grid[0])
    # path = [0 for _ in range(k)]

    # def dfs(step, index):
    #     if step == k:
    #         nonlocal result
    #         result = min(result, total)
    #         return

    #     if index < n:
    #         path[step] = index
    #         dfs(step + 1, index)
    #     if index < n + 1:
    #         path[step] = index + n
    #         dfs(step + 1, index + n)

    # result = total
    # dfs(0, 0)
    # return result

    def bfs(k):
        queue = []
        visited = [False for _ in range(len(grid))]
        total = 0
        for i in range(k):
            total += grid[i][0] + grid[i][-1]

        queue.append(total)
        visited[0] = True
        visited[-1] = True
        result = [0 for _ in range(k)]
        for i in range(
