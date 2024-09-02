
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
    # only 3x3 grids
    if len(grid) < 2 or len(grid[0]) < 2: return -1

    m, n = len(grid), len(grid[0])
    # ! TLE
    if m * n < k: return -1
    # ! TLE
    if k == 0: return []

    # ! TLE
    if k == m * n: return grid[0][0]

    # create a copy of the grid for path finding
    dst_grid = [[grid[i][j] for j in range(n)] for i in range(m)]
    # create a min heap containing the first row
    min_heap = []
    path = [0] * k
    HEAPTYPE = min

    for i in range(n):
        dst_grid[0][i] = grid[0][i]
        # ! TLE
        if len(min_heap) < k:
            e = HEAPTYPE(dst_grid[0][i])
            min_heap.append(e)
            continue

        # mark the cell as visited
        dst_grid[0][i] = float('inf')
        # update the heap structure
        e = HEAPTYPE(dst_grid[0][i])
        min_heap[0] = e
        _sift_down(min_heap, 0, k - 1)

    # process the rest of the grid
    for i in range(1, m):
        for j in range(n):
            dst_grid[i][j] = min(dst_grid[i - 1][j], dst_grid[i][j - 1]) + grid[i][j]
            # ! TLE
            if len(min_heap) < k:
                e = HEAPTYPE(dst_grid[i][j])
                min_heap.append(e)
                continue

            # mark the cell as visited
            dst_grid[i][j] = float('inf')
            # update the heap structure
            e = HEAPTYPE(dst_grid[i][j])
            min_heap[0] = e