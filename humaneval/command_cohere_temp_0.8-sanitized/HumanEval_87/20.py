def get_row(lst, x):
    res = []
    for row in lst:
        if x in row:
            col = row.index(x)
            res.append((len(lst) - row.index(row) - 1, col))
    res.sort(key=lambda x: (x[0], -x[1]))
    return res