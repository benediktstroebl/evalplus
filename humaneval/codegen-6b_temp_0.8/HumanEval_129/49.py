
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
    # This is a rather simple problem that is very widely used in a competitive
    # game. For example, say you're playing a 2d plane game and you are on the
    # top left corner and you are trying to reach the top right corner.
    # The only way to get there is to go up, down, left, and right. 1, 1 and 1
    # are the three top cells and 4, 1 and 4 are the two ones on the right and
    # bottom cells. Since 4 < 3, and 1 < 1, there are no other cells on which
    # you can go, so you can only go there.
    # Similarly, if the bottom-right corner is in the bottom row, you can only
    # go up.
    #
    # To think about what the solution is, here we need to take into account
    # the boundary of the grid. For a 2d grid, we don't have to worry about
    # that because there are only 4 neighboring cells.
    #
    # The solution is to build a simple graph and use a simple breadth-first
    # search to find the least-connected node (of size k). This is tricky as
    # the graph can have all the nodes because each row/column can have all
    # the possible values. In our case, the graph is a 2d array, and the
    # cells in the grid can each have the same size and values, but this is
    # for a very specific problem.
    #
    # To solve this problem, we can use a min-heap to record the degree of
    # each of the nodes (aka "distance" from the start of the graph). In order
    # to avoid unnecessary visits, we can remove an edge from the graph when
    # there is a cycle (aka the node is visited before we visit it again).
    #
    # The idea is to have the nodes sorted by degree based on which we will
    # visit them (in a greedy manner!). The goal is to visit nodes of the
    # highest degree. Starting with the root of the min-heap, visit a node
    # with the highest degree. If this node has a degree larger than the
    # degree of this visit, don't visit it, do nothing and remove the edge
    # from the graph