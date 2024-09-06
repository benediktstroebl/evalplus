def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = [max(row) for row in lst]
    m = len(rows)
    n = len(cols)
    i = rows.index(x)
    j = cols.index(x)
    while i < m and j < n:
        result.append((i, j))
        try:
            i += 1
        except IndexError:
            j += 1
    return result