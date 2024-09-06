
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
    rows = len(grid)
    cols = len(grid[0])

    # Initialize min path with the cell values of the first row
    min_path = [grid[0][0]]
    visited = set([0, 0])

    for i in range(1, k):
        # If the current path is longer than k, it cannot be the optimal path
        if len(min_path) >= k:
            break

        # Get the possible next positions
        next_positions = [(min_path[-1] - 1) % rows, (min_path[-1] + 1) % rows, min_path[-1] - cols, min_path[-1] + cols]

        # For each possible next position
        for next_position in next_positions:
            # If the next position has not already been visited
            if next_position not in visited:
                # Add the next position to the current path
                min_path.append(next_position)
                visited.add(next_position)

                # If the current path is now of length k, it is optimal, so we return the path
                if len(min_path) == k:
                    return min_path

                break

    # Return the minimum path
    return min_path



