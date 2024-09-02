
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
    # base case
    if k == 1:
        return [grid[0][0]]

    # find the minimum path by BFS
    def bfs(start):
        # queue is used to store all the nodes to be visited
        queue = [[start]]
        # a boolean list is used to mark if a node has been visited or not
        visited = [start]
        # min_path is used to store the minimum path found
        min_path = []

        while queue:
            # dequeue the first node in the queue
            path = queue.pop(0)
            node = path[-1]

            # break if path is found
            if len(path) == k:
                min_path = path
                break

            # traverse the neighbors of the current node
            for new_node in get_neighbors(node):
                # check if the node has been visited
                if new_node not in visited:
                    # if not, mark it and enqueue it
                    visited.append(new_node)
                    path_copy = list(path)
                    path_copy.append(new_node)
                    queue.append(path_copy)

        return min_path

    # helper method to get neighbors of a node
    def get_neighbors(node):
        return [
            (node[0] - 1, node[1] - 1),
            (node[0] - 1, node[1]),
            (node[0] - 1, node[1] + 1),
            (node[0], node[1] - 1),
            (node[0], node[1] + 1),
            (node[0] + 1, node[1] - 1),
            (node[0] + 1, node[1]),
            (node[0] + 1, node[1] + 1)
        ]

    # find the start node
    start = find_start(grid, k)
    # return the minimum path
    return bfs(start)

