
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
    # naive solution
    # when k is large, this solution will take a lot of time to finish
    # can we do better?
    # first we should notice that
    # if we have visited one cell in the previous step
    # we can choose the same cell again
    # so our choices is not just the adjacent cells
    # but it can be the adjacent cells, and also the cell we choose from
    # in the previous step
    # so we can do a dfs with a visited set
    # or use a set of visited cells that we can backtrack to
    # time complexity O(N^3)
    # space complexity O(N^2)
    # this solution passes on leetcode but is too slow

    # do a dfs with a set of visited cells
    # start from the first cell,
    # mark the cell as visited
    # if the length of the path is less than k
    # then we dfs to the adjacent cells
    # we also save the path we took to a list
    # when we backtrack, we also need to save the path we took
    # so that we can add it to the set
    # if we hit a cell that is already in the set
    # we can get the path we took to that cell and also
    # the last step we took
    # we can add the path we took to that cell to the set
    # and add the last step we took
    # return the list of values on the visited cells

    if k == 0:
        return []

    visited = set()
    path = []
    dfs(grid, 0, 0, k, visited, path)
    res = []
    for i in range(k):
        res.append(path[i][1])
    return res

