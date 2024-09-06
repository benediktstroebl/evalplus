
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
    if len(grid) == 0:
        return []
    if k >= len(grid) * len(grid):
        return []
    
    def next_move(pos, visited):
        r, c = pos
        moves = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        new_moves = []
        for move in moves:
            if move[0] >= 0 and move[0] < len(grid) and move[1] >= 0 and move[1] < len(grid):
                if move not in visited:
                    new_moves.append(move)
        return new_moves
    
    queue = [(0, 0, [])]
    visited = set()
    visited.add((0, 0))
    visited.add((1, 0))
    visited.add((0, 1))
    
    while queue:
        r, c, moves = queue.pop(0)
        if len(moves) == k:
            return moves
        if len(moves) > k:
            continue
        for move in next_move((r, c), visited):
            new_moves = list(moves)
            new_moves.append(grid[move[0]][move[1]])
            queue.append((move[0], move[1], new_moves))
            visited.add((move[0], move[1]))
