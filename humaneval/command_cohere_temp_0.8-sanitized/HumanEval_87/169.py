def get_row(matrix, x):
    result = []
    for row in matrix:
        for j, val in enumerate(row):
            if val == x:
                result.append((row_num, col_num))
                break
        row_num += 1
    result.sort(key=lambda x: (x[1], x[0]))
    return result