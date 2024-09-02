
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

    # Store the coordinates of the cells already visited
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    # Initialize the path to the first cell of the grid
    path = [grid[0][0]]
    # Check for backtracking
    if not visited[0][0]:
        return []
    # Store the values of the cells in the path
    values = []
    # Add the value of the current cell to the path
    values.append(grid[path.index(grid[0][0])][0])
    # Add the path to the list of the minimum path
    min_path.append(values)
    # Mark the cell as visited
    visited[path.index(grid[0][0])][0] = True
    # Recursively find the minimum path in the rest of the grid
    for i in range(1, len(grid)):
        # Find the next cell to visit
        j = 0
        for k in range(i):
            if not visited[k][j]:
                next_cell = grid[k][j]
                path.append(next_cell)
                values.append(next_cell)
                visited[k][j] = True
                break
        else:
            return min_path
        # Add the path to the list of the minimum path
        min_path[-1].append(values)
        values = [grid[i][j] for i in path for j in range(len(grid[i]))]

    return min_path