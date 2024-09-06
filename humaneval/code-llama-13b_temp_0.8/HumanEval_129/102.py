
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
    # can we do a dp solution here?
    # the last k cells visited?
    if k == 0:
        return []

    rows = len(grid)
    cols = len(grid[0])

    if rows == 0 or cols == 0:
        return []

    def get_cell(pos):
        return grid[pos[0]][pos[1]]

    def get_neighbors(pos):
        neighbors = []
        x, y = pos

        # left
        if x > 0:
            neighbors.append((x - 1, y))

        # top
        if y > 0:
            neighbors.append((x, y - 1))

        # right
        if x < rows - 1:
            neighbors.append((x + 1, y))

        # bottom
        if y < cols - 1:
            neighbors.append((x, y + 1))

        return neighbors

    def find_paths(start_pos, length, last_k_visited):
        paths = []

        if length == 0:
            return [list(last_k_visited)]
        elif length < 0:
            return []

        for neighbor in get_neighbors(start_pos):
            neighbor_val = get_cell(neighbor)
            if neighbor_val not in last_k_visited:
                # append to last_k_visited
                last_k_visited.append(neighbor_val)

                # now check this neighbor
                neighbor_paths = find_paths(neighbor, length - 1, last_k_visited)
                last_k_visited.pop()

                if neighbor_paths:
                    for neighbor_path in neighbor_paths:
                        paths.append(neighbor_path)

        return paths

    paths = find_paths((0, 0), k, [])
    min_path = min(paths)
    return min_path

