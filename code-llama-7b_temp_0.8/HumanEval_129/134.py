
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
    Algorithm:
    - Check if k is greater than or equal to N
    - Do the following for each cell, with DFS:
        1. Visit the cell
        2. Check if the cell's index is greater than k
        3. If the cell's index is less than or equal to k, then return the cell's value
        4. Check if the cell is at the boundary of the grid
        5. If not at the boundary, then for each of the neighboring cells, recursively
           go down the tree, and append the cell's value to the list

    Complexity:
    Time: O(N^2)
    Space: O(N^2)
    """
    def helper(grid, k, curr_pos, visited, path, curr_k):
        if curr_k == 0:
            return

        # visit the cell
        curr_k -= 1

        # check if the cell's index is greater than k
        if curr_k <= 0:
            return

        # check if the cell's index is less than or equal to k
        if curr_k <= 0:
            path.append(grid[curr_pos[0]][curr_pos[1]])
            return

        # check if the cell is at the boundary of the grid
        if curr_pos[0] <= 0 or curr_pos[1] <= 0 or \
           curr_pos[0] >= len(grid) - 1 or curr_pos[1] >= len(grid[0]) - 1:
            return

        # if not at the boundary, then for each of the neighboring cells,
        # recursively go down the tree, and append the cell's value to the list
        helper(grid, k, (curr_pos[0] + 1, curr_pos[1]), visited, path, curr_k)
        helper(grid, k, (curr_pos[0] - 1, curr_pos[1]), visited, path, curr_k)
        helper(grid, k, (curr_pos[0], curr_pos[1] + 1), visited, path, curr_k)
        helper(grid,
