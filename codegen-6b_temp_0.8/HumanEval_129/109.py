
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
    row = len(grid)
    col = len(grid[0])
    if row == 1 and col == 1:
        return [grid[0][0]]

    from operator import itemgetter
    adj = [[0]*col for _ in xrange(row)]
    for i in xrange(row):
        for j in xrange(col):
            adj[i][j] = grid[i][j]

    def dfs(current_x, current_y, k):
        if k == 1:
            return sorted(adj[current_x][current_y])
        else:
            current_value = adj[current_x][current_y]
            min_cell = [current_value]
            adj[current_x][current_y] = float('inf')
            for d in DIRECTIONS:
                next_x, next_y = current_x+d[0], current_y+d[1]
                if 0 <= next_x < row and 0 <= next_y < col:
                    if adj[next_x][next_y] < current_value:
                        min_cell = dfs(next_x, next_y, k-1)
            adj[current_x][current_y] = current_value
            return sorted(min_cell + current_value)

    result = dfs(0, 0, k)
    for r in result:
        print r,
    print

