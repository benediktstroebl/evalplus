def minPath(grid, k):
    n = len(grid)
    visited = set()
    q = [(-1, 0)]  # (-1, cell) indicates the starting cell with value -1
    path = []

    while len(q) > 0:
        dist, cell = heappop(q)

        if dist > k:
            continue

        if k == dist:
            path.extend(cell)
            break

        if cell not in visited:
            visited.add(cell)
            neigbs = [(dist + 1, c) for c in [(cell[0] - 1, cell[1]), (cell[0] + 1, cell[1]), (cell[0], cell[1] - 1), (cell[0], cell[1] + 1)]]
            heappush(q, *neigbs)

    # Remove -1 from the beginning of the path
    path = [cell for cell in path if cell != -1]
    return path
def heappop(q):
    return heapq.heappop(q)