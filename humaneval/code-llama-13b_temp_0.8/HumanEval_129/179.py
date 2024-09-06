
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
    if not grid:
        return []
    
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    queue = deque([(0, 0)])
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    visited[0][0] = True
    heap = [(0, 0)]
    dist = [grid[0][0]]

    while queue:
        cur_cell = queue.popleft()
        dist.append(grid[cur_cell[0]][cur_cell[1]])
        visited[cur_cell[0]][cur_cell[1]] = True
        if len(dist) == k:
            return dist
        for dire in directions:
            row = cur_cell[0] + dire[0]
            col = cur_cell[1] + dire[1]
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and not visited[row][col]:
                queue.append((row, col))
                visited[row][col] = True
                heapq.heappush(heap, (grid[row][col], row, col))
    
    while len(dist) < k:
        val, row, col = heapq.heappop(heap)
        dist.append(val)

    return dist

