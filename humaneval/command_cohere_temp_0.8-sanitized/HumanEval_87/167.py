def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_index + 1, column_index + 1))
                column_index += 1
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result