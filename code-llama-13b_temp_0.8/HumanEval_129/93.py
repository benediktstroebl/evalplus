
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

    def getNeighbours(current):
        (i, j) = current
        neighbours = [(i, j-1), (i, j+1), (i+1, j), (i-1, j)]
        neighbours = [neigh for neigh in neighbours if
                      neigh[0] >= 0 and neigh[0] < rows and neigh[1] >= 0 and neigh[1] < cols]
        return neighbours

    def minPathHelper(current, k, visited):
        if k == 0:
            return current
        visited.add(current)
        neighbours = getNeighbours(current)
        neighbour_visited = list(filter(lambda neigh: neigh in visited, neighbours))
        unvisited = [neigh for neigh in neighbours if neigh not in visited]
        if not unvisited:
            return []
        unvisited.sort(key=lambda x: grid[x[0]][x[1]])
        return [grid[current[0]][current[1]]] + minPathHelper(unvisited[0], k-1, visited)

    rows = len(grid)
    cols = len(grid[0])
    min_paths = []
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                min_path = minPathHelper((i, j), k, visited)
                if min_path:
                    min_paths.append(min_path)
    min_paths.sort()
    return min_paths[0]

