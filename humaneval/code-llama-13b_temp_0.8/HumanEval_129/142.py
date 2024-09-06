
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
    visited = [[False for _ in range(N)] for _ in range(N)]
    neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    curr_row, curr_col = 0, 0
    next_row, next_col = 0, 0
    best_path = []
    best_cost = -1
    cost = 0
    while curr_row < N and curr_col < N:
        # Explore current cell
        # print("Current:", (curr_row, curr_col))
        for i in range(4):
            next_row = curr_row + neighbors[i][0]
            next_col = curr_col + neighbors[i][1]
            # print("Next:", (next_row, next_col))
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            # print("Visited:", visited[next_row][next_col])
            if not visited[next_row][next_col]:
                cost += grid[next_row][next_col]
                # print("Cost:", cost)
                if best_cost == -1 or cost < best_cost:
                    best_cost = cost
                    best_path.append(grid[next_row][next_col])
                curr_row, curr_col = next_row, next_col
                # print("Current:", (curr_row, curr_col))
                break
        visited[curr_row][curr_col] = True
        # print("Current:", (curr_row, curr_col))
        cost -= grid[curr_row][curr_col]
        # print("Cost:", cost)

    return best_path

