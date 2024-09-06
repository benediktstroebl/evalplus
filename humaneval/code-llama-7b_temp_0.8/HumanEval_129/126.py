
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
    if not grid: return []
    R, C = len(grid), len(grid[0])
    # only O(n) space
    dp = [[float('inf') for _ in range(C)] for _ in range(R)]
    dp[0][0] = 0
    for k in range(1, k+1):
        # O(n^2) space
        next_dp = [[float('inf') for _ in range(C)] for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if k == 1 and r == 0 and c == 0: continue
                next_dp[r][c] = float('inf')
                if r > 0:
                    next_dp[r][c] = min(next_dp[r][c], dp[r-1][c])
                if c > 0:
                    next_dp[r][c] = min(next_dp[r][c], dp[r][c-1])
                if r < R-1:
                    next_dp[r][c] = min(next_dp[r][c], dp[r+1][c])
                if c < C-1:
                    next_dp[r][c] = min(next_dp[r][c], dp[r][c+1])
                next_dp[r][c] += grid[r][c]
        dp = next_dp
    ans = []
    r, c = R-1, C-1
    while r >= 0 and c >= 0:
        ans.append(grid[r][c])
        if dp[r-1][c] == dp[r][c]:
            r -= 1
        elif dp[r][c-1] == dp[r][c]:
            c -= 1
        elif dp[r+1][c] == dp[r][c]:
            r += 1
        else:
            c += 1
    ans.reverse()
    return ans
