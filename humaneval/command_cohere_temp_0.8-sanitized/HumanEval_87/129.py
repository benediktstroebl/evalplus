def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = [max(row) for row in lst]
    for i, r in enumerate(lst):
        for j, c in enumerate(r):
            if c == x:
                result.append((i, j))
    result.sort(key=lambda x: (rows.index(x[0]), cols.index(x[1])))
    return result