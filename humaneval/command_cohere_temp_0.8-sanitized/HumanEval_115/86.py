import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)
    
    if capacity > wells:
        return 0
    
    if capacity == 1:
        return sum(sum(row) for row in grid)
    
    def dp(row):
        n = len(row)
        res = [0] * n
        for i in range(1, n):
            max_i = 0
            for j in range(i):
                if row[j] + row[max_i] <= capacity:
                    max_i = max(max_i, j)
            res[i] = 1 + max(res[j] for j in range(i) if row[j] + row[i] <= capacity)
        return res
    
    def solve(row, col, cap):
        if col == wells:
            return sum(row) <= cap
        if col < 0 or col >= wells or row[col] == 0:
            return 0
        return max(solve(row, col + 1, cap), solve(row, col + 1, cap - row[col]), dp(row)[col])
    
    return max(solve(grid, 0, capacity), solve(list(zip(*grid))[1], 0, capacity))