
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
    if not grid or not grid[0]:
        return []

    n, n_row, n_col = len(grid), len(grid[0]), len(grid[0][0])
    size = n * n + 1
    min_path_cnt = min(n_row, n_col)
    cur_min_path_cnt = min_path_cnt - 1
    best_path_cnt = size - min_path_cnt
    output = [size]

    heap = [(0, ((0, 0), size - 1))]
    visited = {}
    while heap:
        cur_path_cnt, cur_path = heapq.heappop(heap)

        cur_x, cur_y = cur_path[-1]
        if cur_path_cnt == cur_min_path_cnt:
            cur_val = grid[cur_x][cur_y]
            best_path_cnt = min(best_path_cnt, size - cur_path_cnt)
            output.append(cur_val)
            continue

        if cur_path_cnt > cur_min_path_cnt:
            break

        visited[cur_path] = True

        # find all neighbors
        for neighbor in [(cur_x + x, cur_y + y) for x, y in DIRECTIONS]:
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n_col and (not visited.get(neighbor) or neighbor == cur_path[0]):
                new_path_cnt = cur_path_cnt + 1
                new_path = tuple(sorted(cur_path + (neighbor,)))

                if neighbors_less_than_best(new_path, best_path_cnt):
                    # heapq.heappush(heap, (new_path_cnt, new_path))
                    heap.append((new_path_cnt, new_path))

    if best_path_cnt == size:
        return output
    return output[:best_path_cnt + 1]


assert minPath([[1, 2,