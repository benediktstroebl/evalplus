
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
    # for a matrix of m rows and n cols, the node of row r, col c is r * n + c
    # and that of row r, col 0 is r * n.
    # the row of node i is (i // n), and col of node i is (i % n)

    def neighbors(node):
        # return a list of the neighbor nodes of node.
        r = node // n
        c = node % n
        if r > 0:
            yield r * n + c
        if r < m - 1:
            yield (r + 1) * n + c
        if c > 0:
            yield r * n + c - 1
        if c < n - 1:
            yield r * n + c + 1

    def key(path):
        return (len(path), path)

    n = len(grid[0])
    m = len(grid)
    if m * n != len(set(i for j in grid for i in j)):
        return None
    if k > m * n:
        return None
    if k < 1:
        return None

    q = []
    q.append((0, ()))
    memo = {}
    while q:
        path_len, path = heapq.heappop(q)
        if len(path) == k:
            return list(path)
        if len(path) > k:
            continue
        node = path[-1]
        for nbr in neighbors(node):
            if nbr not in path:
                new_path_len = path_len + 1 + abs(grid[nbr // n - (node // n)] - grid[nbr // n])
                new_path = path + (nbr,)
                if new_path_len not in memo or key(memo[new_path_len]) > key(new_path):
                    memo[new_path_len] = new_path
                    heapq.heappush(q, (new_path_len, new_path))
    return None
