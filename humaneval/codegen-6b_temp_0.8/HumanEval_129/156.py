
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
    # all neighbors in 4 directions
    neighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    
    rows = len(grid)
    cols = len(grid[0])
    
    # preprocess grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                grid[i][j] = float('inf')
    
    # store visited cells
    seen = {}
    
    # find minimum path
    def dfs(n, m, seen, path):
        # find minimum path
        if len(path) == k:
            return path
        
        min_path = float('inf')
        for n_n in neighbors:
            i = n + n_n[0]
            j = m + n_n[1]
            
            if i >= 0 and i < rows and j >= 0 and j < cols:
                if i not in seen or j not in seen:
                    seen[i] = seen[j] = True
                    min_path = min(min_path, grid[i][j])
                    seen[i] = seen[j] = False
        
        # find minimum path from min_path
        if min_path != float('inf'):
            leftover_min_path = dfs(n, m, seen, path + [min_path])
            if leftover_min_path != float('inf'):
                return leftover_min_path
        
        return float('inf')
    
    
    return dfs(0, 0, seen, [])

