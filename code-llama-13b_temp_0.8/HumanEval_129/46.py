
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
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return []
    
    def is_valid(i, j):
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
            return True
        return False

    def find_neighbors(i, j):
        neighbors = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_i = i + x
            n_j = j + y
            if is_valid(n_i, n_j):
                neighbors.append((n_i, n_j))
        return neighbors

    INF = float("inf")
    min_path_length = {(i, j): INF for i in range(len(grid)) for j in range(len(grid[0]))}
    min_path_length[(0, 0)] = 0
    start = (0, 0)
    end = (len(grid)-1, len(grid[0])-1)

    q = deque([start])
    while q:
        i, j = q.popleft()
        for n_i, n_j in find_neighbors(i, j):
            new_path_length = min_path_length[(i, j)] + grid[n_i][n_j]
            if new_path_length < min_path_length[(n_i, n_j)]:
                min_path_length[(n_i, n_j)] = new_path_length
                q.append((n_i, n_j))

    return min_path_length[end]

