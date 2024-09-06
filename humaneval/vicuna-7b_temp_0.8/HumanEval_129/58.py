
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
    # Check if the input is valid.
    if not 1 <= grid.shape[0] <= grid.shape[1] or not 1 <= grid[0].shape[0] <= grid[0].shape[1]:
        return []
    
    # If the grid is empty, return an empty list.
    if not grid:
        return []
    
    # Creating a dictionary to count the number of ways to reach each cell.
    count = {}
    for row in grid:
        for cell in row:
            count[cell] = count.get(cell, 0) + 1
    
    # Creating a list to store the minimum path.
    path = []
    
    # The minimum cost of the path is the key to the minimum cost of the dictionary.
    min_cost = float('inf')
    
    # The path starts from the first cell.
    path_cost = grid[0][0]
    
    # iterating through each cell in the grid
    for cell in grid:
        # If the cell is already on the path, increment the cost.
        path_cost = max(path_cost + 1, count[cell])
        path.append(cell)
        # if the cost of the current cell is less than the minimum cost,
        # update the minimum cost and path
        if path_cost < min_cost:
            min_cost = path_cost
            # Adding the current cell to the path
            path.insert(0, cell)
    
    # The path is the ordered list of the cells that the minimum path go through.
    return path