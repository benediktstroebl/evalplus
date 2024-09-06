
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
    def cell_min_path(cell, lst, k):
        if k == 0:
            return lst
        # check if k is less than the length of the string
        if k < len(cell):
            # return cell if k is equal to the length of the string
            if k == len(cell):
                return cell
            # find the value that's less than k
            min_val = min(cell[:k])
            # return the new cell and the new lst
            return [min_val] + cell_min_path(cell[cell.index(min_val):], lst + [min_val], k - 1)
        else:
            # if k is greater than the length of the string, find the index of the first value that is not less than k
            for idx, val in enumerate(cell):
                if val >= k:
                    return cell_min_path(cell[idx + 1:], lst + [val], k)

    if not grid: return []
    if not grid[0]: return []
    return cell_min_path(grid[0], [], k)

