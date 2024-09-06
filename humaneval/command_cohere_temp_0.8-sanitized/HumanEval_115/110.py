import math
def max_fill(grid, capacity):
    bucket = 0
    row, col = len(grid), len(grid[0]) 
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                bucket_fill = 0
                start_row, start_col = i, j
                for ni, nj in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                    if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1:
                        bucket_fill += 1
                        start_row, start_col = ni, nj
                        if bucket_fill == capacity:
                            return bucket + bucket_fill - 1
                            break
                grid[start_row][start_col] = 0
                bucket += bucket_fill
    return bucket
capacity = 1