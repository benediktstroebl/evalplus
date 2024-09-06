
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
    def is_valid(coord, grid):
        r, c = coord
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def is_visited(coord, visited):
        r, c = coord
        return (r, c) in visited

    def make_dist(grid, k):
        cur = [grid[r][c] for r in range(len(grid)) for c in range(len(grid[0]))]
        for i in range(1, k):
            pre = cur[:len(cur) - i]
            pre.sort()
            cur = [pre[0]] + cur[len(cur) - i:]
        return cur

    def is_in_k(cur, k):
        return len(cur) == k

    def is_equal(cur, k):
        lst = [[str(i) for i in cur]]
        for _ in range(k):
            lst.append([])
            for row in lst:
                for i in range(len(row)):
                    for j in range(i + 1, len(row)):
                        if row[i] > row[j]:
                            return False
                        row[i], row[j] = row[j], row[i]
        return True

    def is_valid_in_k(cur, k):
        cur.sort()
        return is_in_k(cur, k) and is_equal(cur, k)

    def split_path(path):
        out = [[]]
        for i in range(1, len(path)):
            if path[i - 1] < path[i]:
                out[-1].append(path[i - 1])
                out.append([path[i]])
        return out

    def make_path(path):
        if len(path) == 0:
            return []
        return path[-1] + make_path(path[:-1])

    def gen_paths():
        paths = []
        vv = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r