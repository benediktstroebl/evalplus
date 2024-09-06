
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
    # initialize n rows and n columns as the size of grid
    n = len(grid)
    # initialize a priority queue with heapq
    heap = []
    # append all the values in the first row in the heap
    for i in range(n):
        heapq.heappush(heap, (grid[0][i], 0, i))
    # append the min value in the first row to the result
    result = [heap[0][0]]
    # initialize a set to check if we have seen the cell before
    seen = {(0, i) for i in range(n)}
    # iterate for k steps
    for _ in range(k):
        # pop the cell with the minimum value
        value, row, col = heapq.heappop(heap)
        # append the current value to the result
        result.append(value)
        # check if we are not on the edge of the grid
        if row != 0:
            # add the cell on the top to the heap
            heapq.heappush(heap, (grid[row-1][col], row-1, col))
            # check if the cell has been seen before
            if (row-1, col) in seen:
                # remove the cell from the heap
                heapq.heappop(heap)
            # add the cell to the seen set
            seen.add((row-1, col))
        # check if we are not on the edge of the grid
        if col != n-1:
            # add the cell on the right to the heap
            heapq.heappush(heap, (grid[row][col+1], row, col+1))
            # check if the cell has been seen before
            if (row, col+1) in seen:
                # remove the cell from the heap
                heapq.heappop(heap)
            # add the cell to the seen set
            seen.add((row, col+1))
    return result
