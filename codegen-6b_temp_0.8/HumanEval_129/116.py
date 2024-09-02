
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
    """
    # recursive, slow
    if k == 1:
        return [1]
    
    # init
    n = len(grid)
    m = len(grid[0])
    # base case
    if k == n * m:
        return [grid[i][j] for i in range(n) for j in range(m)]
    
    # recursive case
    # 1. init
    visited = [[False] * m for i in range(n)]
    visited[0][0] = True
    # 2. topdown
    # recursive helper
    def helper(row, col):
        # base case
        if row >= n or col >= m:
            return 0
        # 3. update visited
        if not visited[row][col]:
            visited[row][col] = True
            # 1. calc left
            left = helper(row, col + 1)
            # 2. calc top
            top = helper(row + 1, col)
            # 3. calc right
            right = helper(row, col - 1)
            # 4. calc bottom
            bottom = helper(row - 1, col)
            # 5. return max
            return max(left, top, right, bottom) + grid[row][col]
        # 4. return visited
        return 0
    
    # from row 1 to row n
    res = helper(0, 0)
    return res
    """
    
    # dfs
    res = []
    stack = [(0, 0)]
    while stack:
        row, col = stack.pop(0)
        if len(res) == k:
            break
        # go to left
        if col - 1 >= 0 and not (row, col-1) in res:
            stack.append((row, col-1))
            res.append((row, col-1))
        # go to top
        if row - 1 >= 0 and not (row-1, col) in res:
            stack.append((row - 1, col))
            res.append((row - 1, col))
        # go to right
        if col + 1 < m and not (row, col+1) in res: