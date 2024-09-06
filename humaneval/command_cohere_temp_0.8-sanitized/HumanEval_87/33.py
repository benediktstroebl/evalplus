def get_row(lst, x):
    result = []
    rows = [0, 0, 0]
    for i in range(0, len(lst)):
        row = lst[i]
        row_len = len(row)
        if row_len > rows[0]:
            rows = [row_len, i, row_len - 1]
        elif row_len < rows[0]:
            rows = [row_len, i, row_len]
        while rows[2] >= 0 and x == row[rows[2]]:
            result.append((rows[1], rows[2]))
            rows[2] -= 1
    result.sort()
    for i in range(0, len(result)):
        result[i] = (result[i][0], result[i][1])
    result.sort(key=lambda x: x[1])
    return result