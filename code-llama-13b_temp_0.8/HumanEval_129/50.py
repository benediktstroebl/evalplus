
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
    def get_neighbors(cell, grid):
        r, c = cell
        neighbors = []
        if r > 0:
            neighbors.append((r-1, c))
        if r < len(grid) - 1:
            neighbors.append((r+1, c))
        if c > 0:
            neighbors.append((r, c-1))
        if c < len(grid[r]) - 1:
            neighbors.append((r, c+1))
        return neighbors
    
    def find_next(current, k, grid, visited, distances):
        minimum = (float("inf"), ())
        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited:
                distance = distances[current] + grid[neighbor[0]][neighbor[1]]
                if distance < minimum[0]:
                    minimum = (distance, neighbor)
        return minimum
    
    def get_path(current, visited, grid):
        path = []
        for cell in visited:
            path.append(grid[cell[0]][cell[1]])
        return path
    
    distances = {}
    visited = set()
    current = (0,0)
    visited.add(current)
    distances[current] = 0
    while len(visited) <= k:
        current = find_next(current, k, grid, visited, distances)
        visited.add(current[1])
        distances[current[1]] = current[0]
    return get_path(current[1], visited, grid)

