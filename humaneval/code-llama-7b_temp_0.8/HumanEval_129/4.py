
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
    # We can transform the grid into a graph
    # since every cell is connected to its neighbours
    # We can also use Dijkstra's Algorithm to find the shortest path
    # in this graph

    # Since the goal is to find the path of length k, we have to check the
    # length of each path. There's no point in using Dijkstra's Algorithm
    # if the path is longer than k, since the path will be of length k or less
    # The algorithm will go through each cell and check the path length to
    # each neighbour of that cell.

    # If the path is equal to k, we can just return that path
    # if the path is longer than k, we can just ignore it
    # if the path is shorter than k, we can add it to a queue of shortest paths
    # since we can go to any neighbour at any point
    # We'll check this queue periodically to check for shorter paths

    # There's also the option of BFS
    # the algorithm will do a BFS for every cell and return the shortest path

    # Either way, we can find the shortest path using Dijkstra's Algorithm

    # We can also use dynamic programming.

    # 1. Find the shortest path between the two corners of the grid
    # 2. Find the shortest path between the two corners with a midpoint
    # 3. Find the shortest path between the two corners with a midpoint in the path
    # 4. Repeat steps 2-4 until we can't add any more points in the path

    # We can find the shortest path between any two points using Dijkstra's Algorithm

    # We can use BFS, or Dijkstra's Algorithm
    # Since the total number of cells is limited, we can use a matrix
    # to keep track of the distances

    # The same logic can be used for Dijkstra's Algorithm

    # We can also use memoization
    # In the recursion tree, if we've already calculated a distance,
    # we can just return the distance

    # We can use either BFS or Dijkstra's Algorithm
    # The shortest path
