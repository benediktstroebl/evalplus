
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
    # import pdb; pdb.set_trace()

    # # O(kn^2) time, O(k^2) space
    # # O(k^2) time, O(k^2) space
    # def get_path(start_i, start_j, path_so_far, path_idx):
    #     if path_idx == k:
    #         paths.append(path_so_far)
    #         return

    #     if start_i - 1 >= 0:
    #         get_path(start_i - 1, start_j, path_so_far + [grid[start_i - 1][start_j]], path_idx + 1)

    #     if start_j - 1 >= 0:
    #         get_path(start_i, start_j - 1, path_so_far + [grid[start_i][start_j - 1]], path_idx + 1)

    #     if start_i + 1 < n:
    #         get_path(start_i + 1, start_j, path_so_far + [grid[start_i + 1][start_j]], path_idx + 1)

    #     if start_j + 1 < n:
    #         get_path(start_i, start_j + 1, path_so_far + [grid[start_i][start_j + 1]], path_idx + 1)

    # n = len(grid)
    # paths = []
    # for i in range(n):
    #     for j in range(n):
    #         get_path(i, j, [grid[i][j]], 1)

    # print(paths)
    # return min(paths)

    # # O(kn) time, O(k) space
    # # O(k) time, O(k) space
    # def get_path(i, j, curr_path, curr_path_idx, paths, path_idx):
    #     if curr_path_idx == k:
    #         paths[path_idx] = curr_path
    #         return True

    #     if i - 1 >= 0 and (
    #         paths[path_idx - 1][curr_path
