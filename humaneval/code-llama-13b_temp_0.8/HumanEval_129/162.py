
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
    n = len(grid)
    end = n*n
    x, y = 0, 0
    k_steps = [grid[0][0]]
    k_steps_increasing = [grid[0][0]]
    k_steps_decreasing = [grid[0][0]]

    def find_min_path(x, y, k):
        nonlocal grid
        nonlocal k_steps
        nonlocal k_steps_increasing
        nonlocal k_steps_decreasing

        if k == 1:
            return k_steps

        neighbors = []
        if x > 0 and grid[x - 1][y] <= grid[x][y]:
            neighbors.append((x - 1, y, grid[x - 1][y]))
        if x < n - 1 and grid[x + 1][y] <= grid[x][y]:
            neighbors.append((x + 1, y, grid[x + 1][y]))
        if y > 0 and grid[x][y - 1] <= grid[x][y]:
            neighbors.append((x, y - 1, grid[x][y - 1]))
        if y < n - 1 and grid[x][y + 1] <= grid[x][y]:
            neighbors.append((x, y + 1, grid[x][y + 1]))
        if not neighbors:
            return k_steps

        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            if neighbor[2] in k_steps_increasing and neighbor[2] in k_steps_decreasing:
                k_steps = k_steps_increasing + k_steps_decreasing[::-1]
                return k_steps
            elif neighbor[2] in k_steps_increasing and neighbor[2] not in k_steps_decreasing:
                k_steps_decreasing.append(neighbor[2])
            elif neighbor[2] not in k_steps_increasing and neighbor[2] in k_steps_decreasing:
