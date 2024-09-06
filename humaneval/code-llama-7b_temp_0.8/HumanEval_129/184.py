
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

    # grid: list of lists of integers
    # k: an integer
    # return: a list of integers
    # input and output are not lists or tuples
    # input grid may contain duplicates
    # input k is between 1 and 10^9 inclusive
    # grid is guaranteed to have between 2 and 100 rows and 2 and 100 columns
    # grid values are between 1 and 100 inclusive

    # first, create a dictionary mapping the values in the grid to their locations
    value_to_coordinates = {}
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value in value_to_coordinates:
                value_to_coordinates[value].append((i, j))
            else:
                value_to_coordinates[value] = [(i, j)]

    # then, create a graph where the vertices are values and edges are the distances between
    # each pair of values
    graph = {}
    for value in value_to_coordinates:
        graph[value] = set()
        for neighbor in value_to_coordinates[value]:
            neighbor_value = grid[neighbor[0]][neighbor[1]]
            graph[value].add(neighbor_value)

    # then, create a list of values and distances that are needed to visit to get to
    # the destination
    path = []
    end_value = grid[0][0]
    path.append(end_value)
    next_end_values = graph[end_value]
    next_end_values.remove(path[0])
    i = 1
    while i < k:
        if not next_end_values:
            return []
        next_end_value = next_end_values.pop()
        path.append(next_end_value)
        next_end_values = graph[next_end_value]
        next_end_values.remove(path[i])
        i += 1

    # finally, return the path
    return path

