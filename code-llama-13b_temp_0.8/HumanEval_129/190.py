
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

    grid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    N = len(grid)

    # Cached minimum paths for each value up to k - 1
    min_path_table = [[-1] * N for _ in range(N)]

    def min_path(i, j, curr_len):
        # Already reached the end
        if curr_len == k:
            return []

        # Check if we have a cached answer
        cached_answer = min_path_table[i][j]
        if cached_answer != -1:
            return cached_answer

        # Base case - curr_len == k - 1
        if curr_len == k - 1:
            path = [grid[i][j]]
            min_path_table[i][j] = path
            return path

        paths = []

        # Moving right
        if j < N - 1:
            right_path = min_path(i, j + 1, curr_len + 1)
            paths.append(grid[i][j] + right_path[0])

        # Moving down
        if i < N - 1:
            down_path = min_path(i + 1, j, curr_len + 1)
            paths.append(grid[i][j] + down_path[0])

        # Moving right and down
        if i < N - 1 and j < N - 1:
            right_down_path = min_path(i + 1, j + 1, curr_len + 1)
            paths.append(grid[i][j] + right_down_path[0])

        min_path = min(paths)
        min_path_table[i][j] = min_path
        return min_path

    min_path = min_path(0, 0, 0)
    print(min_path)
    print(min_path_table)


