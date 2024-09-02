
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
    def get_neighbours(cell):
        """
        Returns the neighbours of the cell.

        :param cell: A tuple representing the cell.
        :return: A list containing the neighbours.
        """
        i, j = cell
        neighbours = []
        if i > 0:
            neighbours.append((i - 1, j))
        if i < n - 1:
            neighbours.append((i + 1, j))
        if j > 0:
            neighbours.append((i, j - 1))
        if j < m - 1:
            neighbours.append((i, j + 1))
        return neighbours


    def minPathHelper(grid, k, path, cell, visited, length):
        """
        Recursive helper function to find the minimum path.

        :param grid: A matrix (list of lists) containing the grid.
        :param k: An integer representing the length of the path to find.
        :param path: A list containing the path so far.
        :param cell: A tuple representing the current cell.
        :param visited: A dictionary containing the visited cells.
        :param length: An integer representing the length of the path so far.
        :return: A list containing the minimum path.
        """
        # If the path has reached the desired length, return the path.
        if length == k:
            return path
        # If the current cell has been visited before, return None.
        if cell in visited:
            return None
        # Get the neighbours of the current cell.
        neighbours = get_neighbours(cell)
        # Set the path as visited.
        visited[cell] = True
        # Recursively call the function for each neighbour, and add the cell
        # to the path if a valid path is found.
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            res = minPathHelper(grid, k, path + [grid[neighbour[0]][neighbour[1]]], neighbour, visited, length + 1)
            if res is not None:
                return res
        # Otherwise, set the current cell as un
