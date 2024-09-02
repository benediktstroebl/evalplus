
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
    
    # Apply the Dijkstra's algorithm.
    # We store the lengths of each path in a dictionary, where the keys are the
    # path and the values are the path's lengths.
    queue = [(0, 0, 0, [])]
    length_dict = {}
    while queue:
        # Get the current element and remove it from the queue.
        (cost, row, col, path) = heapq.heappop(queue)
        
        # If the current position (row, col) is not yet visited, 
        # mark it as visited and update the path's length.
        if (row, col) not in length_dict:
            length_dict[(row, col)] = cost
            
            # If the length of the current path is k, then we found the answer.
            if len(path) == k:
                return path
            
            # Add the neighboring positions to the queue.
            if col + 1 < len(grid[0]):
                heapq.heappush(queue, (cost + grid[row][col + 1], row, col + 1, path + [grid[row][col + 1]]))
            if col > 0:
                heapq.heappush(queue, (cost + grid[row][col - 1], row, col - 1, path + [grid[row][col - 1]]))
            if row + 1 < len(grid):
                heapq.heappush(queue, (cost + grid[row + 1][col], row + 1, col, path + [grid[row + 1][col]]))
            if row > 0:
                heapq.heappush(queue, (cost + grid[row - 1][col], row - 1, col, path + [grid[row - 1][col]]))
    
    return None

