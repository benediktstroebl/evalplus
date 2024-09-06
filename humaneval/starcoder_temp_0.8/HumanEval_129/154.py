
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
    N = len(grid)
    if k >= 2*N:
        return [grid[N//2][N//2]]

    path = [grid[N//2][N//2]]
    for _ in range(k-1):
        curr_row = N//2
        curr_col = N//2
        while True:
            # we're out of boundary
            if curr_row == 0 and curr_col == 0:
                break
            # left
            elif curr_col == 0:
                curr_row -= 1
            # up
            elif curr_row == 0:
                curr_col -= 1
            # right
            elif grid[curr_row][curr_col-1] < grid[curr_row][curr_col]:
                curr_col -= 1
            # down
            elif grid[curr_row-1][curr_col] < grid[curr_row][curr_col]:
                curr_row -= 1
            # diagonal up left
            elif grid[curr_row-1][curr_col-1] < grid[curr_row][curr_col]:
                curr_row -= 1
                curr_col -= 1
            # diagonal down right
            elif grid[curr_row-1][curr_col+1] < grid[curr_row][curr_col]:
                curr_row -= 1
                curr_col += 1

        path.append(grid[curr_row][curr_col])

    return path

