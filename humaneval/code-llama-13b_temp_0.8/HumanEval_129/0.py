
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
    # this is a graph traversal problem
    # build a graph
    graph = {}
    for row in grid:
        for col in row:
            graph[col] = []
    # add connections
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j != len(grid[i]) - 1:
                graph[grid[i][j]].append(grid[i][j+1])
            if i != len(grid) - 1:
                graph[grid[i][j]].append(grid[i+1][j])
    # dfs
    # for each new cell add the next k-1 cells to the queue
    # if the new cell is already visited ignore
    # if the cell is a target, compare it with the current min 
    # if lesser than update the min
    n = len(grid) * len(grid[0])
    # sort the graph
    for key in graph.keys():
        graph[key] = sorted(graph[key])
    # initialize min
    min_path = grid[0][0]
    for i in range(1, n):
        min_path = min_path * 10 + grid[0][i]
    # initialize dfs
    queue = [[grid[0][0]]]
    while len(queue) > 0:
        path = queue.pop(0)
        if len(path) == k:
            if path < min_path:
                min_path = path
        else:
            for cell in graph[path[-1]]:
                new_path = path[:]
                new_path.append(cell)
                queue.append(new_path)
    # convert to the answer format
    ans = []
    for digit in str(min_path):
        ans.append(int(digit))
    return ans



