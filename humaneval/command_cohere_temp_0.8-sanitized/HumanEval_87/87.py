def get_row(lst, x):
    result = []
    for row in lst:
        row_len = len(row)
        for j, col in enumerate(row):
            if col == x:
                result.append((row_len-1, row_len-j-1))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result