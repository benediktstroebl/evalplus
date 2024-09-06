def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, value in enumerate(row):
            if value == x:
                result.append((row_index + 1, column_index + 1))
                break
        row_index += 1
    result.sort(key=lambda x: x[1])
    return result