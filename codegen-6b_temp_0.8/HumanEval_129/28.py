
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
    if k == 0:
        return []

    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return []

    # base case
    if k == 1:
        return [grid[0][0]]

    row, col = len(grid), len(grid[0])

    # traverse through each cell
    min_path_list = []
    for i in range(row):
        for j in range(col):
            # try to extend the minimal path from current cell
            path = minPath(grid, k - 1)
            if path:
                # if we could still finish the minimal path
                # add the current cell to it
                min_path_list.append(grid[i][j])
                # skip remaining cells already in minimal path
                for k in range(i, len(min_path_list)):
                    if min_path_list[k] == path[k - i]:
                        break
                    else:
                        continue
                # if we could finish the minimal path
                # add the rest of cells on the right
                for k in range(i, len(min_path_list)):
                    min_path_list.append(grid[i][j + k - i])
                # if we could finish the minimal path
                # add the rest of cells on the left
                for k in range(i, len(min_path_list)):
                    if min_path_list[k - i] == path[k - i]:
                        break
                    else:
                        continue
                # if we could finish the minimal path
                # add the rest of cells on the upper
                for k in range(i, len(min_path_list)):
                    if min_path_list[k - i] == path[k - i]:
                        break
                    else:
                        continue
                # if we could finish the minimal path
                # add the rest of cells on the lower
                for k in range(i, len(min_path_list)):
                    if min_path_list[k - i] == path[k - i]:
                        break
                    else:
                        continue

    return min_path_list

