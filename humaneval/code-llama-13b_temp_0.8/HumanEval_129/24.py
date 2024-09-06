
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
    # return the shortest path with the lowest lexicographic order
    def shortestPath(grid, k):
        n = len(grid)
        if k > (n-1)**2:
            return None
        if k == 0:
            return []
        
        shortest_paths = [[None for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(k+1):
                if i == 0 and j == 0:
                    shortest_paths[i][j] = grid[0][0]
                    continue
                if j == 0:
                    shortest_paths[i][j] = shortest_paths[i-1][j]
                    continue
                if i == 0:
                    shortest_paths[i][j] = shortest_paths[i][j-1]
                    continue
                shortest_paths[i][j] = min(shortest_paths[i-1][j], shortest_paths[i][j-1])
        
        return shortest_paths[n-1][k]

    # Find the path to the minimum value in the grid
    def findMinPath(grid):
        min_path = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == shortestPath(grid, (n-1)**2):
                    min_path.append(grid[i][j])
        return min_path

    # Find the lexicographically minimum path with length k
    def findMinPathLengthK(grid, k):
        # Find the path to the minimum path in the grid
        min_path = findMinPath(grid)

        # Find the path that has the same values as min_path and length k
        n = len(grid)
        shortest_paths = [[None for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            for j in range(k+1):
                if i == 0 and j == 0:
                    short
