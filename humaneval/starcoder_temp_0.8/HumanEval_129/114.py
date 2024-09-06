
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
    # # way 1
    # row_count, col_count = len(grid), len(grid[0])
    # grid.append([i for i in range(1, row_count * col_count + 1)])
    # col_sum = [0 for i in range(col_count + 1)]
    # for row_idx in range(row_count):
    #     for col_idx in range(col_count):
    #         col_sum[col_idx + 1] += grid[row_idx][col_idx]
    #         grid[row_idx + 1][col_idx] += col_sum[col_idx] + 1
    # min_path_sum = float('inf')
    # min_path = []
    # for row_idx in range(row_count + 1):
    #     for col_idx in range(col_count + 1):
    #         if row_idx == 0 or col_idx == 0:
    #             continue
    #         for left_idx in range(col_idx - k, col_idx):
    #             right_idx = left_idx + k
    #             if right_idx >= col_count + 1:
    #                 continue
    #             if grid[row_idx][left_idx] < grid[row_idx][right_idx]:
    #                 break
    #             if grid[row_idx][left_idx] > grid[row_idx][right_idx]:
    #                 continue
    #             if left_idx == 0:
    #                 sum_val = grid[row_idx - 1][col_idx] - grid[row_idx][right_idx]
    #             else:
    #                 sum_val = grid[row_idx - 1][left_idx - 1] - grid[row_idx][right_idx]
    #             if sum_val < min_path_sum:
    #                 min_path_sum = sum_val
    #                 min_path = [grid[row_idx][col_idx]]
    #             elif sum_val == min_path_sum:
    #                 min_path.append(grid[row_idx][col_idx])
    # return min_path

    # way 2
    row_count, col_count =
