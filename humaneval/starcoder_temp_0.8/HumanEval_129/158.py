
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
    n = len(grid)
    m = len(grid[0])
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    def find_path(start):
        path = [start]
        cnt = 1
        while cnt < k:
            for x,y in moves:
                if 0 <= start[0]+x < n and 0 <= start[1]+y < m and grid[start[0]+x][start[1]+y] not in path:
                    path.append(grid[start[0]+x][start[1]+y])
                    start = (start[0]+x,start[1]+y)
                    break
            cnt += 1
        return path

    def sort_path(path):
        n = len(path)
        for i in range(n):
            for j in range(i,n):
                if path[i] > path[j]:
                    path[i], path[j] = path[j], path[i]
        return path

    min_path = None
    for i in range(n):
        for j in range(m):
            cur_path = find_path((i,j))
            cur_path = sort_path(cur_path)
            if not min_path or cur_path < min_path:
                min_path = cur_path
    return min_path
