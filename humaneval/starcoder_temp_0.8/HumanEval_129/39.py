
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
    N = len(grid)
    path = []

    # Base case: k is 0, the minimum path is an empty list
    if k == 0:
        return []
    
    # Recursive case: 
    # First, compute the minimum path of length k-1 
    # Second, find the path of length k
    # Third, merge the two paths

    # Step 1: Find the minimum path of length k-1. The minimum path of length k-1
    # is the one that starts at the cell where the minimum path of length k
    # ends. For example, if we have the following grid and the minimum path of
    # length k is [5, 3, 1, 6, 4, 2], then the minimum path of length k-1 
    # will start at the cell [5, 3, 1, 6].
    path.append(min(grid[N-1-k+1][j] for j in range(N)))

    # Step 2: Find the path of length k.
    for i in range(N-k):
        if grid[i][path[-1]-1] < grid[i+k][path[-1]-1]:
            path.append(grid[i][path[-1]-1])
        else:
            path.append(grid[i+k][path[-1]-1])

    # Step 3: Merge the two paths.
    return path
