
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
    def min(a, b):
        return a if a < b else b

    def find_min(grid, k):
        # initialize
        N = len(grid)
        r = 0
        c = 0
        # search min from each cell
        min_val = float('inf')
        min_r = -1
        min_c = -1
        for i in range(0, N):
            for j in range(0, N):
                if grid[i][j] < min_val:
                    min_val = grid[i][j]
                    min_r = i
                    min_c = j
        # perform BFS
        queue = deque()
        visited = [[False for _ in range(N)] for _ in range(N)]
        queue.append((min_r, min_c, k))
        visited[min_r][min_c] = True
        min_val = float('inf')
        min_r = -1
        min_c = -1
        while queue:
            # pop from queue
            r, c, k = queue.popleft()
            if k == 0:
                if grid[r][c] < min_val:
                    min_val = grid[r][c]
                    min_r = r
                    min_c = c
            else:
                # add to queue with k - 1
                # up
                if r - 1 >= 0 and not visited[r - 1][c]:
                    queue.append((r - 1, c, k - 1))
                    visited[r - 1][c] = True
                # right
                if c + 1 < N and not visited[r][c + 1]:
                    queue.append((r, c + 1, k - 1))
                    visited[r][c + 1] = True
                # down
                if r + 1 < N and not visited[r + 1][c]:
                    queue.append((r + 1, c, k - 1))
                    visited[r + 1][c] = True
                # left
                if c - 1 >= 0 and not visited[r][c - 1]:
                    queue.append((r, c - 1, k - 1))
                    visited[r][c - 1] = True
        return min_val, min_r, min_c

    # find
