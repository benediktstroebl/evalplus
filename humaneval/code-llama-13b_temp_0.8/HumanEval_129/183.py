
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
    """
    - LC 983, https://leetcode.com/problems/minimum-cost-for-tickets/
    - LC 689, https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
    - LC 576, https://leetcode.com/problems/out-of-boundary-paths/

    Intuition:
        A brute-force solution is to traverse all the nodes that are reachable with k steps,
        and calculate the minimum paths for each of them.
        A greedy solution is to traverse each node once, in a top-down manner.
        For each node, the minimum path value is obtained by adding the node value to the
        minimum path values for each of its neighbors (up to 4 neighbors for each node).
        The minimum path value is maintained in a priority queue, such that for each node,
        the minimum path value (and the corresponding path) is kept at the top of the priority queue.

        We are interested in the paths that end at some position (x,y), such that x == N-1 and y == N-1.
        If the path is the minimum path for some node (x,y), it is also the minimum path for the node (x+1,y) and (x,y+1).
        Therefore, the correct answer is the minimum path for the node (N-1, N-1).

    Edge Case:
        Points out of the grid

    Key Idea:
        - If we need to compute the minimum path for each node, we can compute the minimum path for each node that is connected to the grid boundary.
        - For each such node, the minimum path is the minimum among its neighbors plus the node value.
        - For each such node, we will have to maintain the minimum paths for its neighbors plus the node value.
        - Since we only care about the minimum path for the grid boundary, we can ignore all the other nodes.
        - We do not need to actually compute the path, just compute the path sum.
        - For each node, only the neighbor nodes that are connected to the grid boundary have the minimum path sum.
