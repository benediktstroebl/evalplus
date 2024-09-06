
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
    
    rows = len(grid)
    cols = len(grid[0])

    if rows < 2 or cols < 2:
        return [grid[0][0]]

    visited = set()
    min_path_visited = []
    path = []

    def is_valid(x, y):
        return (x >= 0 and x < rows and y >= 0 and y < cols and (x, y) not in visited)

    def get_min_path(x, y, k):
        if k <= 0:
            return 0

        if not is_valid(x, y):
            return 0

        visited.add((x, y))

        value = grid[x][y]

        if x == 0 and y == 0:
            min_path_visited.append(value)

        min_path = float('inf')
        for x_offset, y_offset in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            min_path = min(min_path, get_min_path(x + x_offset, y + y_offset, k - 1))

        min_path_visited.append(value)

        path.append(value)

        return min_path + value

    get_min_path(0, 0, k)

    return path

