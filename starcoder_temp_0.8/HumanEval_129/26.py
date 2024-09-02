
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
    
    N = len(grid)
    # initialize distances from each cell to the start cell as the max possible value
    # so that for each cell, the min distance to the start cell can be easily found
    distances = [[math.inf for j in range(N)] for i in range(N)]
    # distance of each cell from the start cell is zero
    distances[0][0] = 0
    # queue to store tuples of (cell, distance from the start cell)
    q = [(0, 0)]
    while len(q) > 0:
        i, j = q.pop(0)
        # add the distance of this cell from the start cell to the min distance from the start cell
        # the distance from the start cell is initialized as zero, so the min distance is the distance
        # of the current cell from the start cell
        min_distance = distances[i][j]
        # get the neighboring cells
        neighbors = get_neighbors(i, j, N)
        for neighbor in neighbors:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                # update the min distance
                if distances[neighbor[0]][neighbor[1]] > min_distance + grid[neighbor[0]][neighbor[1]]:
                    distances[neighbor[0]][neighbor[1]] = min_distance + grid[neighbor[0]][neighbor[1]]

    # return the distance of the cell which is k steps away from the start cell
    return distances[k-1][k-1]
