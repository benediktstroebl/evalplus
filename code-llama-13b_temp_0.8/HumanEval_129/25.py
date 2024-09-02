
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
    # Remember that minPath(grid, k) is equal to minPath(grid, k-1) plus the min
    # element of the bottom row of the grid.
    # So to get the minPath we just need the min element of minPath(grid, k-1)
    # plus the min element of the bottom row of the grid.
    # To get minPath(grid, k-1) we only need the min element of minPath(grid, k-2)
    # plus the min element of the bottom row of the grid.
    # And so on, until we reach the minPath(grid, 1) which is equal to the min
    # element of the bottom row of the grid.
    #
    # We use a queue to implement the recursion.
    #
    # We also store the path in a list and return it.
    #
    # NOTE: This approach is not very efficient. See the other solutions for
    # better approaches.
    #
    # Time Complexity: O(nk)
    # Space Complexity: O(nk)
    from collections import deque

    queue = deque()
    # This is the min path we are searching for.
    path = []
    # This is the current path we are exploring.
    current_path = [grid[0][0]]
    # This is the current position we are exploring.
    current_x = 0
    current_y = 0
    # This is the current minimum path.
    current_min_path = grid[0][0]
    # This is the current minimum path length.
    current_min_path_length = 0
    # This is the number of elements we still need to process.
    elements = grid[0][0]
    for i in range(1, k):
        # This is the next element.
        elements += grid[0][i]
        # Add the next element to the path.
        current_path.append(grid[0][i])
        # If we are in the last row...
        if i == grid[0][-1]:
            # Add the next element to the path.
            path.append(grid[0][i])
            # Update
