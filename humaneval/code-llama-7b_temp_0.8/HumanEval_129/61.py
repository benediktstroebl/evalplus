
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
    # the problem is not very clear about what is the path.
    # for example, for the input [ [5,9,3], [4,1,6], [7,8,2]], k = 2
    # does this mean the path is [5, 9] or [5, 1]?
    # assuming the path is [5, 9], the output should be [5, 9, 3]
    # assuming the path is [5, 1], the output should be [5, 9, 1]
    # so the problem needs to be reworded.
    # a simple way to find the minimum path is to perform the following:
    # 1. for each column, find the maximum value in the column
    # 2. for each row, find the maximum value in the row
    # 3. find the minimum value among the maximum values in the columns
    # 4. find the minimum value among the maximum values in the rows
    # 5. find the minimum value among the maximum values in both the columns and the rows
    # 6. repeat step 3, 4 and 5 until the k is reduced to 1
    # 7. return the path

    if grid is None or len(grid) == 0 or len(grid[0]) == 0:
        return []

    if k == 1:
        return [min(max(i) for i in grid)]

    # max_cols = [max(i) for i in zip(*grid)]
    # max_rows = [max(i) for i in grid]
    # min_values = min(max_cols + max_rows)

    # cols = list()
    # rows = list()

    # for index in range(len(grid)):
    #     max_values = list()
    #     for i in grid[index]:
    #         if i == min_values:
    #             max_values.append(i)
    #     cols.append(max_values)

    # for index in range(len(grid[0])):
    #     max_values = list()
    #     for i in range(len(grid)):
    #         if
