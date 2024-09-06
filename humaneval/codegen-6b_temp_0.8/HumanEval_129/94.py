
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
    if k == 0:
        return [grid[0][0]]

    row_num = len(grid)
    col_num = len(grid[0])

    # Build a min-heap with the cell values as the value, (row, col) as the key
    heap = []
    for row in range(row_num):
        for col in range(col_num):
            heap.append((grid[row][col], (row, col)))
    heapq.heapify(heap)

    # Build the min-heap back
    tree = []
    for _ in range(k):
        tree.append(heapq.heappop(heap)[0])

    # At the end the heap contains the smallest k values
    # Now recursively merge the values
    while k > 1:
        # pop the first and last values
        x1, c1 = heapq.heappop(heap)
        x2, c2 = heapq.heappop(heap)

        # merge the two
        new_val = tree[-1] + tree[-2]
        heapq.heappush(heap, (new_val, (c1[0], c2[1])))

        # update the tree
        tree.append(x1 + x2)

        # move to the next ring
        k -= 1

    return tree

