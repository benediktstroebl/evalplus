def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_idx + 1, col_idx + 1))
                break
        row_idx += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))