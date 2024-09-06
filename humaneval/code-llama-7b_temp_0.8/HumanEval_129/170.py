
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
    # O(n)
    min_path = []
    grid_sorted = []
    for row in grid:
        grid_sorted.append(sorted(row))
    grid_sorted_sorted = []
    grid_sorted_sorted.append(grid_sorted[0])
    for i in range(1, len(grid_sorted)):
        current_row = []
        for j in range(len(grid_sorted[i])):
            current_row.append(grid_sorted[i][j])
            if j > 0:
                current_row.append(grid_sorted[i][j - 1])
            if j < len(grid_sorted[i]) - 1:
                current_row.append(grid_sorted[i][j + 1])
        grid_sorted_sorted.append(sorted(current_row))
    k = min(k, len(grid) + len(grid[0]) - 1)
    for i in range(1, len(grid_sorted_sorted)):
        for j in range(len(grid_sorted_sorted[i])):
            if j == 0:
                min_path.append(grid_sorted_sorted[i][j])
                break
            elif grid_sorted_sorted[i][j] < grid_sorted_sorted[i][j - 1]:
                min_path.append(grid_sorted_sorted[i][j])
                break
    return min_path[-k:]
