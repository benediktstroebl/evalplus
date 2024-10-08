
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
    # first find the stop point
    all_nodes = [i for i in range(N * N) if grid[i // N][i % N] == '*']
    if k < len(all_nodes):
        stop_point = all_nodes[k - 1]
    else:
        return []

    # use DFS to generate the topologically sorted nodes, if k is 1, we can return the result directly
    if k == 1:
        return [grid[i // N][i % N] for i in range(N * N) if grid[i // N][i % N] != '*']

    # if not reach the stop point, we need to recursively then insert the stop point to the result
    result = []
    for i in range(N * N):
        if grid[i // N][i % N] != '*':
            grid[i // N][i % N] = '*'
            result.append(i)
            if i == stop_point:
                break

    # now we can generate the result
    if len(result) == k:
        return result

    visited = [False for _ in range(N * N)]
    def dfs(node):
        # we should only visit the nodes that are not visited
        if not visited[node]:
            visited[node] = True
            for node_ in neighbors(node, grid, visited):
                dfs(node_)
            return

    # we will visit all the non-stop nodes
    for node in range(N * N):
        visited[node] = True
        dfs(node)
        if len(result) < k:
            result.append(node)

    return result


grid = [
    ['c', 'a', 'a', 'a'],
    ['b', 'a', 'a', 'a'],
    ['a', 'a', 'a', 'a'],
    ['a', 'a', 'a', 'a'],
    ['a', 'a', 'a', 'a'],
    ['a', 'a', 'a', 'a'],
    ['a', 'a', 'a', 'a'],
