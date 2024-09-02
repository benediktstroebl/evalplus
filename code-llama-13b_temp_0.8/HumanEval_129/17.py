
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
    # Write your code here

    # Start at top left cell
    # Find optimal path that uses smallest numbers at each step
    # Find optimal path at each node by comparing each neighbor node's path
    # with current path. 
    # If path is not optimal, return False. 

    # At each iteration:
        # Visit current node
        # At each neighbor node:
            # If neighbor is not visited and neighbor path is less than current path:
                # Mark neighbor path as optimal
                # Set current path to neighbor path
                # Mark current node as visited

    # At end of iteration, if a path has been found:
        # Return path
    # Otherwise:
        # Return False

    visited = set()
    path = []
    path_score = 0
    current_node = (0, 0)

    while len(path) < k:

        path.append(grid[current_node[0]][current_node[1]])
        path_score += grid[current_node[0]][current_node[1]]
        visited.add(current_node)

        neighbors = get_neighbors(current_node, visited, grid, k)
        neighbor_scores = [grid[node[0]][node[1]] for node in neighbors]
        neighbor_scores.sort()
        # print(f"neighbors: {neighbors}")
        # print(f"neighbor_scores: {neighbor_scores}")

        for i, node in enumerate(neighbors):
            # print(f"Comparing {neighbor_scores[i]} to {path_score}")
            if neighbor_scores[i] < path_score:
                path = [grid[node[0]][node[1]]]
                path_score = 0
                for j in range(len(path)):
                    path_score += path[j]
                current_node = node
                break

        # print(f"Current node: {current_node}")
        # print(f"Path: {path}")

    return path
