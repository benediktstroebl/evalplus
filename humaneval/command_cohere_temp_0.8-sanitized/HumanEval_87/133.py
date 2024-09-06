def get_row(lst, x):
    result = []
    for row in lst:
        for j, col in enumerate(row):
            if col == x:
                result.append((row_index + 1, column_index + 1))
                row_index += 1
                column_index = 0
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    return result