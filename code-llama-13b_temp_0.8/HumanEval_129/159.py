
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
    def isValidCell(cell):
        return cell[0] >= 0 and cell[0] < N and cell[1] >= 0 and cell[1] < N
    def getNeighbours(cell):
        neighbours = []
        if isValidCell([cell[0] + 1, cell[1]]):
            neighbours.append([cell[0] + 1, cell[1]])
        if isValidCell([cell[0] - 1, cell[1]]):
            neighbours.append([cell[0] - 1, cell[1]])
        if isValidCell([cell[0], cell[1] + 1]):
            neighbours.append([cell[0], cell[1] + 1])
        if isValidCell([cell[0], cell[1] - 1]):
            neighbours.append([cell[0], cell[1] - 1])
        return neighbours
    
    N = len(grid)
    C = [[[] for j in range(N)] for i in range(N)]
    Q = []
    for i in range(N):
        for j in range(N):
            C[i][j] = [i,j]
            Q.append([i,j])
    
    while Q:
        cell = Q.pop(0)
        neighbours = getNeighbours(cell)
        for n in neighbours:
            if grid[n[0]][n[1]] < grid[cell[0]][cell[1]]:
                C[cell[0]][cell[1]] = C[n[0]][n[1]]
                Q.append(cell)
            else:
                C[n[0]][n[1]] = C[cell[0]][cell[1]]
                Q.append(n)
    
    ans = []
    k += 1
    while k > 0:
        ans.append(grid[C[0][0][0]][C[0][0][1]])
        C[0][0] = C[C[0][0][0]][C[0][0][1]]
        k -= 1
    
