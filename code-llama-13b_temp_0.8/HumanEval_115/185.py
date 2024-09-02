
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    
    # Get the grid size
    n = len(grid)
    m = len(grid[0])
    # Get the capacities
    x, y = get_capacities(grid, capacity)
    
    # Create the movement matrix
    A = []
    for i in range(m+n):
        A.append([])
        for j in range(m+n):
            A[i].append(0)
    # Create the matrix to store the path
    p = [[0 for _ in range(m+n+1)] for _ in range(m+n+1)]
    # Populate the matrix with the graph
    for i in range(m):
        for j in range(n):
            if i != 0:
                A[i][j] += grid[i][j]
            if j != 0:
                A[j][i] += grid[j][i]
            if i != m-1:
                A[m+i][j] += grid[i][j]
            if j != n-1:
                A[j][m+i] += grid[j][i]
    # Calculate the path
    d = max_fill_fill(A, p, m+n)
    # Calculate the moves
    moves = d[m+n-2][m+n-1]
    # Return the path
    return moves, p

