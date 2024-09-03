def minPath(grid, k):
    """
    Given a grid with N rows and N columns (N>=2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    Returns: ordered list of the values on the cells that the minimum path of length k go through.

    Examples:
        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """
    if not (len(grid) >= 2) or k < 1:
        raise ValueError("Input grid is not a valid grid with rows >1 or k <1")

    # Initialize the minimum path as an empty list
    minPath = [ ]

    # Initialize the visited cells as an empty set
    visited = set()

    # Traverse the grid using Depth-First Search
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in visited:
                continue
            visited.add(grid[i][j])
            minPath.append(grid[i][j])

    return minPath