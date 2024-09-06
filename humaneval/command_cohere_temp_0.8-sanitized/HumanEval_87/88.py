def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = [[row.index(y) for y in row] for row in lst]
    ix = rows.index(x)
    result.extend([(ix, c) for c in cols[ix]])
    result.sort()
    return result