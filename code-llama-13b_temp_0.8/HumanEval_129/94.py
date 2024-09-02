
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
    """
    Intuition:
        DP

    Approach:
        Bottom up, using 2-D dp array to store the solution
        Iterate from the bottom-right corner to the top-left corner
        The boundary conditions are:
            - dp[x][y] = [(y+1, x)] if y > 0
            - dp[x][y] = [(y, x+1)] if x > 0
        The core idea is to use a min-heap to find the k smallest values
        in the neighborhood of (x, y) to get the candidate paths

        We can either traverse the path from left to right or right to left

    Edge Cases:
        - If the number of columns or rows is < 2:
            - return None

    Time Complexity:
        O(k*n) where n is the number of rows and columns

    Space Complexity:
        O(n) since we are storing at most n values in the heap at any time
    """
    def get_min_path(dp, x, y, k):
        path = []
        while x > 0 or y > 0:
            if x > 0 and (y == 0 or dp[x-1][y] < dp[x][y-1]):
                x -= 1
            else:
                y -= 1
            path.append(grid[x][y])
        return path[::-1]

    if len(grid) < 2 or len(grid[0]) < 2:
        return None

    n = len(grid)
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    heap = []
    heapq.heappush(heap, (grid[-1][-1], n-1, n-1))
    for i in range(n):
        dp[i][i] = 1

    while heap:
        cost, x, y = heapq.heappop(heap)
        for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1
