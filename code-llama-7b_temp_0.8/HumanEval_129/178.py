
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
    from queue import PriorityQueue
    def create_graph(matrix, m, n):
        graph = {}
        for i in range(m):
            for j in range(n):
                node = str(i) + ',' + str(j)
                graph[node] = {}

                if i > 0:
                    neighbors = str(i-1) + ',' + str(j)
                    graph[node][neighbors] = matrix[i-1][j]
                if i < m-1:
                    neighbors = str(i+1) + ',' + str(j)
                    graph[node][neighbors] = matrix[i+1][j]
                if j > 0:
                    neighbors = str(i) + ',' + str(j-1)
                    graph[node][neighbors] = matrix[i][j-1]
                if j < n-1:
                    neighbors = str(i) + ',' + str(j+1)
                    graph[node][neighbors] = matrix[i][j+1]
        return graph

    def get_path(graph, start_node, end_node, k, parents, nodes_in_path, path_length):
        if start_node == end_node:
            path_length += graph[start_node][end_node]
            parents[end_node] = parents.get(end_node, start_node)
            nodes_in_path.append(end_node)
            return path_length, parents, nodes_in_path
        if path_length + graph[start_node][end_node] > k:
            return None, parents, nodes_in_path
        path_length += graph[start_node][end_node]
        parents[end_node] = parents.get(end_node, start_node)
        nodes_in_path.append(end_node)
        for neighbor in graph[end_node]:
            if neighbor not in nodes_in_path:
                get_path(graph, start_node, neighbor, k, parents, nodes_in_path, path_length)
