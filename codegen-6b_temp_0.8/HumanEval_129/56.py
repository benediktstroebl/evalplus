
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
    if k == 0 or len(grid) == 0:
        res = []
    elif len(grid) == 1:
        res = [grid[0][0]]
    else:
        # TLE
        # lst = []
        # for i in xrange(len(grid)):
        #     for j in xrange(len(grid[0])):
        #         # print(i, j)
        #         # print(grid[i][j])
        #         lst.append(grid[i][j])
        # lst.sort()
        # print(lst)
        # res = [lst[0]]
        # for i in xrange(1, len(lst)):
        #     if lst[i] <= lst[i - 1]:
        #         lst[i - 1] += 1
        #     else:
        #         lst[i] += 1
        #         res.append(lst[i])
        # print(res)
        # lst.sort(reverse=True)
        # print(lst)
        # res = [lst[0]]
        # for i in xrange(1, len(lst)):
        #     if lst[i] <= lst[i - 1]:
        #         lst[i - 1] += 1
        #     else:
        #         lst[i] += 1
        #         res.append(lst[i])
        # print(res)
        # # TLE
        # visited = set([(0,0)])
        # lst = []
        # res = []
        # path = set([(0,0)])
        # visited_lst = []
        # def dfs(node):
        #     i, j = node
        #     lst.append(grid[i][j])
        #     for nrow, ncol in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        #         if 0 <= i + nrow < len(grid) and 0 <= j + ncol < len(grid[0]):
        #             if (