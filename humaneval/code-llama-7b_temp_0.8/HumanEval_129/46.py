
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
    # set up two dimentional lists of numbers (call them visited)
    # (one for start position, one for end position)
    visited = [[False for i in range(n)] for j in range(n)]
    visited_end = [[False for i in range(n)] for j in range(n)]
    # set up two dimentional lists of possible previous moves
    # (call them previous)
    # (one for start position, one for end position)
    previous = [[None for i in range(n)] for j in range(n)]
    previous_end = [[None for i in range(n)] for j in range(n)]
    # set up lists of steps from start to end position
    # (call them steps)
    steps = [[None for i in range(n)] for j in range(n)]
    # set up lists of values from start to end position
    # (call them values)
    values = [[None for i in range(n)] for j in range(n)]
    # set up lists of moves (call them moves)
    moves = [[None for i in range(n)] for j in range(n)]
    # set up lists of moves (call them moves)
    moves_end = [[None for i in range(n)] for j in range(n)]
    # set up two-dimentional list of lists (call them graph)
    graph = [[None for i in range(n)] for j in range(n)]
    # set up two-dimentional list of lists (call them graph_end)
    graph_end = [[None for i in range(n)] for j in range(n)]
    # set up a list of two-dimentional lists of lists (call them paths)
    paths = []
    # initialize lists for graph and paths
    for row in range(n):
        for col in range(n):
            graph[row][col] = []
            graph_end[row][col] = []
            paths.append([])
    # set up lists for visited and paths
    for row in range(n):
        for col in range(n):
            visited[row][col] = False
            visited_
