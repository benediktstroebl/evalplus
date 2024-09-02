
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
    # here is just a basic implementation
    def get_neighbor(row, col):
        neighbors = []
        if row - 1 >= 0:
            neighbors.append((row - 1, col))
        if row + 1 < N:
            neighbors.append((row + 1, col))
        if col - 1 >= 0:
            neighbors.append((row, col - 1))
        if col + 1 < N:
            neighbors.append((row, col + 1))
        return neighbors
    
    N = len(grid)
    start = (0, 0)
    end = (N - 1, N - 1)
    queue = [start]
    # the path of the grid: it is a set of tuples representing the (row, col)
    path = set([])
    visited = set([])
    while queue:
        # we select the first one in the queue and it is removed
        cur_node = queue.pop(0)
        # we check the current one
        if cur_node == end:
            # if it is the end, we stop
            break
        # we check all the neighbors
        for neighbor in get_neighbor(*cur_node):
            # we check if we have visited the neighbor or not
            if neighbor not in visited:
                # if not, we append it to the path and add it to the queue
                path.add(neighbor)
                queue.append(neighbor)
        # finally, we mark the current node as visited
        visited.add(cur_node)

    # so we have the path, which is a list of tuples (row, col)
    # we need to change it into a list of values
    values = []
    for item in sorted(path):
        values.append(grid[item[0]][item[1]])
    print(values)
    # we need to sort the values (lexicographically)
    for i in range(k - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if values[j] > values[j +
