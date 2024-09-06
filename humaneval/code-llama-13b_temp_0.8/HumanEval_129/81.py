
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
    if len(grid) == 0:
        return []
    nums = range(1, len(grid) * len(grid[0]) + 1)
    nums_list = list(nums)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = nums_list.pop(0)

    # make a path through the matrix
    def dfs(visited, path, k):
        path_len = len(path)
        if path_len == k:
            return True
        if path_len > k:
            return False
        if path_len == 0:
            path.append(grid[0][0])
            if dfs(set([(0, 0)]), path, k):
                return path
            path.pop()
            return False

        row = path[-1][0]
        col = path[-1][1]
        visited.add((row, col))

        # make a dfs search through the matrix
        for i in range(max(0, row - 1), min(row + 2, len(grid))):
            for j in range(max(0, col - 1), min(col + 2, len(grid[0]))):
                if (i, j) not in visited:
                    path.append(grid[i][j])
                    if dfs(visited, path, k):
                        return path
                    path.pop()
        return False

    res = dfs(set([]), [], k)
    if res is False:
        return []
    return res

