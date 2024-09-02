
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
    assert k >= 1
    n = len(grid)
    assert n >= 2

    def get_path(grid, k):
        from collections import defaultdict, deque
        row, col = 0, 0
        visited = defaultdict(lambda: deque(maxlen=k))
        visited[row, col].append(grid[row][col])

        while visited:
            next_queue = deque()

            while visited[row, col]:
                value = visited[row, col].popleft()
                for row, col in neighbors(grid, row, col):
                    if (row, col) not in visited:
                        next_queue.append((row, col))
                    visited[row, col].append(value)

            row, col = next_queue.popleft()

        return visited[row, col]

    def neighbors(grid, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (0 <= row + i < n) and (0 <= col + j < n):
                    yield row + i, col + j

    return get_path(grid, k)

