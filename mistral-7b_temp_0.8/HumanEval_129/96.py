
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
    # We are solving this problem using Dijkstra's algorithm
    # We are constructing an adjacency list, where each cell is a node.
    # Each node has a value, which is the number of the grid cell that the
    # node represents. The value is also used as the key.
    # In this list, we are storing the neighbors of each node, where the neighbors
    # are the nodes that are connected to the current node by an edge.
    # The weight of each edge is 1.
    # We are also storing the distance from the source to each node.
    # The distance is initialized to infinity for all nodes except the source node,
    # which has a distance of 0.
    # We are using a priority queue to keep track of the nodes that have not been visited yet.
    # We are using a heap to implement the priority queue.
    # The priority queue is used to keep track of the nodes that have the smallest distance from the source.
    # We are using a dictionary to keep track of the distances from the source to each node.
    # We are also storing the predecessor of each
