
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
    #####################
    # PSEUDOCODE COMMENT
    #####################
    # This is a modified version of the longest increasing path problem.
    # Similar to a longest increasing path, we need to maintain 2 lists, 
    # one for max and one for min paths.
    # We do this by keeping track of the predecessors (part 2 of the graph)
    # and the values on each node (part 1 of the graph).
    # This will give us the max and min paths in each cell
    # This way, we can trace back to the origin to find the kth cell
    # In other words, we will maintain the kth value of the min path
    # and the kth value of the max path.
    # As long as we maintain the predecessors and the values in a similar
    # fashion, we can extend to a solution for the longest increasing path
    # problem.
    # This gives us the time complexity of O(n^2).
    # The space complexity is also O(n^2).
    #####################
    # PSEUDOCODE COMMENT
    #####################
    # Complexity analysis: 
    # Time complexity: O(N*N). We visit each cell exactly once.
    # Space complexity: O(N*N). 
    #####################
    # FIXME CODE IMPLEMENTATION
    #####################
    def dfs(i, j, k, predecessors, values):
        # Base case: k == 0
        if k == 0:
            predecessors[i][j] = i, j
            return
        # Check to see if we've passed the edge of the matrix
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            return
        # Check to see if the value of the current cell is less than the kth value
        # If the current cell is not a valid cell, we will return 
        if values[i][j] < k:
            return
        # Check to see if the current cell is less than the kth value
        # If it is not, we will return
        if values[i][j
