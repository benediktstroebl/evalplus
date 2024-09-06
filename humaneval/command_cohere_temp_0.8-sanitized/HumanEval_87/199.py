def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_index + 1, column_index + 1))
                break
        row_index += 1
    return sorted(result, key=lambda x: (x[0], -x[1]))