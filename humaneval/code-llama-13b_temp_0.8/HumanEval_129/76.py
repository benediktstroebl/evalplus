
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
    # build a graph for the grid
    graph = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            graph.append([grid[i][j], i, j])
    # Sort the graph by the value
    graph.sort()
    # For each value we add a node to the graph
    graph = [x + [i] for i, x in enumerate(graph)]
    # init the dp
    dp = [[None for _ in range(len(grid) * len(grid[0]))] for _ in range(len(grid) * len(grid[0]) + 1)]
    # init the start
    dp[0] = [[None for _ in range(len(grid) * len(grid[0]))] for _ in range(2)]
    # For each node in the graph we find the min path that end in this node
    for node in graph:
        # get the value
        value = node[0]
        # get the row
        row = node[1]
        # get the col
        col = node[2]
        # get the index of the node
        i = node[3]
        # init the path
        path = [None] * 2
        # for each possible position in the graph
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == row and c == col:
                    continue
                # init the length of the path
                length = None
                # init the prev node
                prev = None
                # find the path between the current node and the node (r, c)
                for n in range(len(graph)):
                    # get the value
                    v = graph[n][0]
                    # get the row
                    x = graph[n][1]
                    # get the col
                    y = graph[n][2]
                    # get the index of the node
                    j = graph[n][3]
                    # if they are equal
                    if r == x and c == y:
                        length = 0
                        prev = j
                    elif (r
