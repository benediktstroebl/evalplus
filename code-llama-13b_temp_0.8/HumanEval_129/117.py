
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
    def getNeighbors(cell, grid, N):
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        neighbors = []
        for direction in directions:
            row = cell[0] + direction[0]
            col = cell[1] + direction[1]
            if row >= 0 and row < N and col >= 0 and col < N:
                neighbors.append((row, col))
        return neighbors

    def isValidCell(cell, grid, N):
        if cell[0] < 0 or cell[0] >= N or cell[1] < 0 or cell[1] >= N:
            return False
        return True

    def getPath(grid, cell, visited, length, N):
        if cell not in visited:
            visited.append(cell)
        neighbors = getNeighbors(cell, grid, N)
        if len(visited) == length:
            return True
        for neighbor in neighbors:
            if getPath(grid, neighbor, visited, length, N):
                return True
        return False

    def createPath(grid, cell, visited, length, N):
        if cell not in visited:
            visited.append(cell)
        neighbors = getNeighbors(cell, grid, N)
        if len(visited) == length:
            return visited
        min_path = []
        for neighbor in neighbors:
            if neighbor not in visited:
                path = createPath(grid, neighbor, visited, length, N)
                if len(path) > 0 and (len(min_path) == 0 or path < min_path):
                    min_path = path
        return min_path

    N = len(grid)
    cell_1 = (0, 0)
    cell_2 = (0, 0)
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 1:
                cell_1 = (row, col)
            elif grid[row][col] == 2:
                cell_2 = (
