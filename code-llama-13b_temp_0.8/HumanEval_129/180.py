
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
    # A: Brute force solution O(n^2*k) space O(n*k)
    # - iteratively put in each of the starting points
    # - then go through each of the paths
    # - if the path is shorter than the min path, then update the min path
    # B: Recursive solution O(n^2*k) space O(n*k)
    # - same as brute force but iterative to recursive
    # C: DP solution O(n^2) space O(n^2)
    # - create the dp table of n * n
    # - init the min path to inf
    # - fill in the first column
    # - for each cell in the grid
    #     - if the cell is not a starting cell, update the min path to
    #     min(min path, curr cell path + curr cell val)
    # - return the min path
    # REF: https://leetcode.com/problems/minimum-path-in-a-grid-ii/discuss/60021/Python-DP-solution
    from collections import deque
    dp = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
    min_path = [float('inf')] * k
    dp[0][0] = grid[0][0]
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                dp[nr][nc] = min(dp[nr][nc], grid[nr][nc] + dp[r][c])
                if dp[nr][nc] == k:
                    queue.append((nr, nc))
                elif dp[nr][nc] < k:
                    min_path = min(min_path, [grid[nr][nc] + v for v in min_path])
    
