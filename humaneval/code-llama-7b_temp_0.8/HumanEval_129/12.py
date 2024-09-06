
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
    #--A--B--C--D--
    #--E--F--G--H--
    #--I--J--K--L--
    #--M--N--O--P--
    #Same as 1506. Find Root of a Matrix 
    #build the search tree (for the first k steps)
    #then construct the path by walking backwards up the tree
    #return the path and reverse it
    
    from collections import defaultdict
    #init
    k -= 1
    root = defaultdict(list)
    leaves = []
    rows = len(grid)
    cols = len(grid[0])
    min_val = 0

    #build the search tree
    for row in range(rows):
        for col in range(cols):
            if row == 0 and col == 0:
                root[0] = [row, col]
                leaves.append([row, col])
                continue

            min_val = grid[row][col]
            min_row = row
            min_col = col
            for row_diff, col_diff in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                new_row = row + row_diff
                new_col = col + col_diff
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_val = grid[new_row][new_col]
                    if new_val < min_val:
                        min_val = new_val
                        min_row = new_row
                        min_col = new_col
            leaves.append([min_row, min_col])
            root[grid[min_row][min_col]].append([min_row, min_col])
            k -= 1
            if k < 0:
                break

    #construct the path
    path = []
    leaf = leaves.pop()
    while leaf is not None:
        path.append(grid[leaf[0]][leaf[1]])
        leaf = root[grid[leaf[0]][leaf[1]]].pop()

    
