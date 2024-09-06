def minPath(grid, k):
    n = len(grid)
    visited = [set() for _ in range(n)]
    q = [([0, 0], 0)]  # Position and value
    while q:
        pos, value = heappop(q)  # Get the cell with the minimum value
        if len(visited[pos[0]][pos[1]]) == k:
            return [value] * k
        visited[pos[0]].add(pos[1])
        for nei in [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]:
            if 0 <= nei[0] < n and 0 <= nei[1] < n and nei[0] != pos[0] and nei[1] != pos[1] and nei not in visited[pos[0]]:
                heappush(q, (nei, value))
    return []
def heappop(q):
    return heapq.heappop(q)