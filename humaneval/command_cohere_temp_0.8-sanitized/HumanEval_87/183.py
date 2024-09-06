def get_row(lst, x):
    res = []
    for i, row in enumerate(lst):
        if x in row:
            res.append((i, row.index(x)))
    return sorted(res, key=lambda x: x[0])