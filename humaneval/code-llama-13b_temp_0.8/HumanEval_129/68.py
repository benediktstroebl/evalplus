
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
    # if k is 1 then return the first row
    if k == 1:
        return grid[0]
    # if k is equal to the number of cells then return the last row
    if k == len(grid) * len(grid[0]):
        return grid[-1]
    # if k is greater than or equal to the number of cells then return the last row
    if k >= len(grid) * len(grid[0]):
        return grid[-1]
    
    # first row of the grid
    first_row = grid[0]
    # last row of the grid
    last_row = grid[-1]
    # last column of the grid
    last_col = [row[-1] for row in grid]

    # initialise the initial list with values from the first row
    init_list = first_row
    # initialise the index
    idx = 0

    while True:
        # next list is the left column
        if idx == 0:
            next_list = [row[idx] for row in grid]
        # next list is the last row
        if idx == len(grid[0]) - 1:
            next_list = last_row
        # next list is the last column
        if idx == len(grid[0]):
            next_list = last_col

        # for each element of the next list, find the minimum
        # element that can be obtained by visiting an adjacent element
        for i in range(len(next_list)):
            next_list[i] = min(init_list[i], init_list[i + 1])

        # if the next list is the last one, then we have reached the end
        if next_list == last_row or next_list == last_col:
            break
        # make the initial list the next list
        init_list = next_list
        # increment the index
        idx += 1

    return next_list


