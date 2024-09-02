
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
    # create a 2d array that keeps the number of times that a number has been selected
    times_selected = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            times_selected[i][j] = grid[i][j]

    # create a 2d array that keeps the lowest number that can be used
    next_number = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]
    def select_number(row, col):
        for i in range(len(grid[0])):
            if times_selected[row][i] < next_number[row][col]:
                next_number[row][i] = times_selected[row][i] + 1
            if i != col:
                if times_selected[i][col] < next_number[row][col]:
                    next_number[row][col] = times_selected[i][col] + 1

    # initialise the array
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i != 0 and j != 0:
                select_number(i,j)

    # store a list that keeps track of the number of times a number has been used
    selected_numbers = [0] * (len(grid) * len(grid[0]))

    # keep track of the sequence of numbers
    sequence = []

    # initialise the sequence
    for i in range(k):
        m = 1
        for j in range(len(grid)):
            for h in range(len(grid[0])):
                if times_selected[j][h] < next_number[j][h]:
                    m = grid[j][h]
        sequence.append(m)
        selected_numbers[m - 1] += 1
        next_number = [[1 for i in range(len(grid[0]))] for j in range(len(grid))]
        select_number(i,j)

