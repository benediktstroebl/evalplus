
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

    # AA: BFS
    # NB: values go from 1 to N*N
    #     1) store values as keys, paths as values in a dictionary
    #     2) at each step, check if we are at the target value
    #     3) if we are, find paths to all neighbors (moves)
    #     4) if the neighbor value is not in the dictionary, put it there as a
    #        new key, with value being the same as the key, but with a new move
    #     5) if the neighbor value is in the dictionary, find the current path
    #        to it and add the move from the current value to the neighbor
    #        value to the path
    #     6) if the neighbor value is in the dictionary, and the path to the
    #        neighbor value is less than the current value, update the dictionary
    #        and the new path as the key.
    #     7) return the path for the target value
    # Time: O(N*N)
    # Space: O(N*N)
    def bfs(grid, k):
        from collections import defaultdict
        if not grid:
            return []
        N = len(grid)
        target = N * N
        # paths as values and values as keys
        d = defaultdict(str)
        d[grid[0][0]] = "U" + d[grid[0][0]]
        q = deque([(0, 0, grid[0][0], d[grid[0][0]])])
        while q:
            i, j, val, path = q.popleft()
            if val == target:
                return list(map(int, list(path)))
            for r, c in [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]:
                if 0 <= r < N and 0 <= c < N:
                    neighbor = grid[r][c]
                    new_path = path + moves[val][neighbor]
                    if neighbor not in d or new_path < d[neighbor]:
                        d[neighbor] = new_path
