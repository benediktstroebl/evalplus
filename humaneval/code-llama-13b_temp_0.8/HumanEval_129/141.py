
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
    ## Solution using priority queue
    class Cell(object):
        def __init__(self, x, y, val):
            self.x = x
            self.y = y
            self.val = val

        def __lt__(self, other):
            if len(self.val) == len(other.val):
                for i in range(len(self.val)):
                    if self.val[i] < other.val[i]:
                        return True
                    if self.val[i] > other.val[i]:
                        return False
            else:
                return len(self.val) < len(other.val)

    import heapq

    heap = []
    heapq.heapify(heap)

    # Calculate cell value
    def getValue(k):
        if k == 0:
            return []
        return [grid[i][j] for i in range(len(grid)) for j in range(len(grid[i])) if i + j == k]

    # Calculate cells with top k lowest values
    def getKCells(heap, k):
        if k == 0:
            return []
        return [heapq.heappop(heap) for _ in range(k)]

    # Add cells to heap
    def addKCells(heap, k, n):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                heapq.heappush(heap, Cell(i, j, getValue(n - grid[i][j])))

    # Find shortest path
    def findPath(heap, k, n):
        if k == 0:
            return []
        if n == 0:
            return []
        kCells = getKCells(heap, k)
        res = []
        for i in range(k):
            res.append(kCells[i].val)
            n -= grid[kCells[i].x][kCells[i].y]
            addKCells(heap, k - (i + 1), n)
            # print(heap)
        return
