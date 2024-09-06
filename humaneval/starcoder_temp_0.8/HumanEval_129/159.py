
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
    if n <= 1:
        return grid

    if k >= n * n:
        return list(chain.from_iterable(grid))

    # we will use a heap structure to store the tuples (lst, dist)
    # for every lst, we want to know the min dist
    # for every dist, we want to know the min lst
    # since the dist is the size of the lst, we will use a list to represent
    # a tuple (dist, lst)

    # to build an entry (lst, dist), we need to know how to compare dist
    # and lst, so we will use a tuple to represent the lst, since tuples
    # are immutable, we need a pair of (dist, lst) where dist is the size
    # of the lst

    # to find the min entry in a heap, we will use heappop(heap)
    # to remove and return the smallest entry in a heap, we will use
    # heappush(heap, entry) to add an entry to a heap

    heap = [((0, []), (0, grid[0]))]

    for _ in range(k - 1):

        min_entry = heappop(heap)
        lst = min_entry[1][1]
        dist = min_entry[1][0]

        if dist == n * n - 1:
            return list(lst)

        row = dist // n
        col = dist % n

        if row + 1 < n:
            heappush(heap, (min_entry[0], (min_entry[1][0] + 1, lst + [grid[row + 1][col]])))

        if col + 1 < n:
            heappush(heap, (min_entry[0], (min_entry[1][0] + 1, lst + [grid[row][col + 1]])))

    min_entry = heappop(heap)
    lst = min_entry[1][1]
    dist = min_entry[1][0]

    return list(lst)

