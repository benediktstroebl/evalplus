
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
    # calculate sum of values on each row
    sums = [sum(grid[i]) for i in range(len(grid))]

    # define helper function
    def k_shortest(grid, k, i, j):
        # base case
        if k == 0:
            return []

        # return empty list if k is greater than sum of values on grid
        if k > sums[i]:
            return []

        # return grid[i][j] if k is 1
        if k == 1:
            return [grid[i][j]]

        # initialize result to an empty list
        result = []

        # check if k is greater than the sum of values on the row
        if k <= sums[i]:
            # find the cell in the row with the minimum value
            min_index = sums[i].index(min(sums[i]))
            # add the value of the cell to result
            result.append(grid[i][min_index])
            # update sums[i] by removing the cell with the minimum value
            sums[i][min_index] = float('inf')
            # reduce k by 1
            k -= 1

        # traverse down
        if i + 1 < len(grid) and j < len(grid[0]) - 1:
            result += k_shortest(grid, k, i + 1, j)
        # traverse right
        if i < len(grid) - 1 and j + 1 < len(grid[0]):
            result += k_shortest(grid, k, i, j + 1)

        return result

    # initialize result to an empty list
    result = []
    # find the cell with the minimum value
    min_index = min(sums).index(min(sums))
    # add the value of the cell to result
    result.append(grid[0][min_index])
    # update sums by removing the cell with the minimum value
    sums[0][min_index] = float('inf')
    # reduce k by 1
    k -= 1
    # find the cell with the minimum value
    min_index = min(sums
