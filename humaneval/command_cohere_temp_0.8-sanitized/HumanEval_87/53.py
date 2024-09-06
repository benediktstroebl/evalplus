def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = []
    for row in lst:
        cols.append(len(row))
    for i, r_cols in enumerate(cols):
        if r_cols == x:
            result.append((i+1, r_cols))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result