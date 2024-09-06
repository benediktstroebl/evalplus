
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
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_squares = num_rows * num_cols
    visited = {}
    visited[0] = [[-1]*num_cols for _ in range(num_rows)]

    def find_min_path(idx, k):
        if k == 0:
            return []
        if idx == num_squares:
            return None

        if k in visited[idx]:
            return visited[idx][k]

        min_path = None
        for i in range(num_cols):
            for j in range(num_rows):
                new_idx = i * num_rows + j
                new_k = k - 1
                cur_path = find_min_path(new_idx, new_k)
                if cur_path is None:
                    continue
                if min_path is None:
                    min_path = cur_path
                elif is_less(cur_path, min_path):
                    min_path = cur_path
        visited[idx][k] = min_path
        return min_path + [grid[idx % num_rows][idx // num_rows]]

    def is_less(a, b):
        if len(a) < len(b):
            return True
        if len(a) > len(b):
            return False
        for i in range(len(a)):
            if a[i] < b[i]:
                return True
            if a[i] > b[i]:
                return False
        return False

    min_path = find_min_path(0, k)
    return min_path


