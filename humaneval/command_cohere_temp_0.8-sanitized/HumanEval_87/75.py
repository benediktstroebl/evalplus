def get_row(lst, x):
    result = []
    for row in lst:
        if x in row:
            col = row.index(x)
            result.append((len(lst) - row.index(row) - 1, col))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result