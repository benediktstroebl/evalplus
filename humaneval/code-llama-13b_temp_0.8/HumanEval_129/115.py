
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
    result = []
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell == 1:
                result = [cell]
                break
        if result:
            break
    visited[r][c] = 1
    r = r - 1
    c = c - 1
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(result) < k and not r < 0 and not c < 0 and not r >= rows and not c >= cols:
        min_value = 100
        for dir in dirs:
            rr = r + dir[0]
            cc = c + dir[1]
            if not rr < 0 and not cc < 0 and not rr >= rows and not cc >= cols:
                value = grid[rr][cc]
                if value < min_value and visited[rr][cc] == 0:
                    min_value = value
                    new_r = rr
                    new_c = cc
        result.append(min_value)
        visited[new_r][new_c] = 1
        r = new_r
        c = new_c
    return result


    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]


    [5, 9, 3],
    [4, 1, 6],
    [7, 8, 2]
