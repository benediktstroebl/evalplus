
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
    if not grid or not grid[0]:
        return []

    # add all values to a list
    values = []
    for row in grid:
        for val in row:
            values.append(val)
    values = sorted(values)

    # global grids
    global_grids = {}
    global_selected_nodes = []

    path = []
    nodes = []
    has_visited = {}

    def dfs(node, path):
        if node in visited:
            return
        if len(path) == k:
            return
        visited.add(node)
        path.append(node[0])
        if len(path) == k:
            return

        for neigh in node[1:]:
            dfs(neigh, path)
            if len(path) == k:
                return

        path.remove(node[0])
        if len(path) == k:
            return

    for val in values:
        # add the value to the global grid
        if val not in global_grids:
            global_grids[val] = set()
        global_grids[val].add(len(nodes))

        # add node to global selected nodes
        global_selected_nodes.append(val)

        # start dfs
        if val not in has_visited:
            has_visited[val] = True
            nodes.append('S')
            dfs(nodes, path)
            if len(path) == k:
                return path

            if val in global_selected_nodes:
                path.append(val)
                global_selected_nodes.remove(val)

            nodes.pop()
            has_visited.pop(val)
    return path

