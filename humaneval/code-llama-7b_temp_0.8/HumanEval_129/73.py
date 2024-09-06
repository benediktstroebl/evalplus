
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
    def dfs(grid, visited, node, k, path):
        if k == 0:
            return path

        for next_node in node.get_adjacent(grid):
            if not visited.get(next_node.r, False):
                visited[next_node.r] = True
                path.append(next_node.val)
                return dfs(grid, visited, next_node, k - 1, path)

        return path

    r = len(grid)
    c = len(grid[0])

    class Node:
        def __init__(self, r, c, val):
            self.r = r
            self.c = c
            self.val = val

        def get_adjacent(self, grid):
            adj = []
            if self.r > 0:
                adj.append(Node(self.r - 1, self.c, grid[self.r - 1][self.c]))
            if self.c > 0:
                adj.append(Node(self.r, self.c - 1, grid[self.r][self.c - 1]))
            if self.r < r - 1:
                adj.append(Node(self.r + 1, self.c, grid[self.r + 1][self.c]))
            if self.c < c - 1:
                adj.append(Node(self.r, self.c + 1, grid[self.r][self.c + 1]))

            return adj

    visited = {}
    visited[0] = True
    node = Node(0, 0, grid[0][0])
    return dfs(grid, visited, node, k - 1, [])
