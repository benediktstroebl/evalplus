
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
    n, m = len(grid), len(grid[0])
    def get_node(i, j, k):
        k += 1
        if k == n + 1:
            return (grid[i][j - k], -1, -1, -1, -1)
        elif j < 1 or j > m:
            return (grid[i][j - k], n + 1, n + 1, n + 1, n + 1)
        elif grid[i][j - k] >= n * n:
            return (grid[i][j - k], n + 1, n + 1, n + 1, n + 1)
        else:
            res = (grid[i][j - k], -1, -1, -1, -1)
            for i_ in range(i - 1, i + 2):
                for j_ in range(j - 1, j + 2):
                    if (i_ != i or j_ != j) and 0 <= i_ < n and 0 <= j_ < m:
                        cur = get_node(i_, j_, k)
                        for idx in range(5):
                            if cur[idx] < res[idx]:
                                res = cur
            return res

    values = get_node(0, m, 0)
    result = []
    for k in range(k):
        if values[1] == -1:
            break
        elif values[0] >= n * n:
            result.append(values[0])
            values = get_node(values[1], values[2], values[3])
        else:
            result.append(values[0])
            values = get_node(values[1], values[2], values[3])
    return result

