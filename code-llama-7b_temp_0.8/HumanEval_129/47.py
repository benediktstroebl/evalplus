
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
    path_count = {}
    path_count[(0,0)] = 1
    min_path = None
    min_count = N*N
    for _ in range(k):
        path_count_new = {}
        for i in range(N):
            for j in range(N):
                if (i,j) in path_count:
                    count = path_count[(i,j)]
                    if count < min_count:
                        min_count = count
                        min_path = grid[i][j]
                    if (i-1 >= 0):
                        path_count_new[(i-1,j)] = path_count_new.get((i-1,j),0) + count
                    if (i+1 < N):
                        path_count_new[(i+1,j)] = path_count_new.get((i+1,j),0) + count
                    if (j-1 >= 0):
                        path_count_new[(i,j-1)] = path_count_new.get((i,j-1),0) + count
                    if (j+1 < N):
                        path_count_new[(i,j+1)] = path_count_new.get((i,j+1),0) + count
        path_count = path_count_new
    return min_path
