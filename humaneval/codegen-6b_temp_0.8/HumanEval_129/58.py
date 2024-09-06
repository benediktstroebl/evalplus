
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
    if not grid or not grid[0] or k == 0:
        return []
    
    # use a heap to store the shortest path from a given cell
    # we keep the shortest path in the top of the tree
    # we also record the current shortest path into the tree
    # since the heap is a min-heap, we can use the following
    # flag to know whether the current path we visit is shorter than the
    # one stored in the heap
    min_heap = []
    
    # we keep prev as a list of list, it will be used to record the previous
    # cell in a given path
    prev = [[] for _ in xrange(len(grid))]
    
    # We used the following to keep track of the visited cells. We start from
    # the first cell, which is the one with the lowest value
    min_heap.append((grid[0][0], 0, 0))
    # we also record the current path in the heap
    result = [(grid[0][0], 0, 0)]
    
    # if we get to the last cell, we return the result
    # in case the current path is more than k, we return the result
    while len(result) < k:
        curr_val, row, col = heapq.heappop(min_heap)
        if row == len(grid) - 1:
            return [curr_val]
        
        # each neighbor can be visited simultaneously when doing a move
        for neighbor in [(row + 1, col), (row, col + 1)]:
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid):
                # we do not want to visit the cell that is already visited
                if neighbor in result:
                    continue
                
                # we visit the cell with a higher value
                if grid[neighbor[0]][neighbor[1]] > curr_val:
                    # we record the cell that we visited
                    result.append((grid[neighbor[0]][neighbor[1]], neighbor[0], neighbor[1]))
                    # we record the current path into the heap
                    heapq.heapp