def get_row(lst, x):
    result = []
    rows = []
    for idx, row in enumerate(lst):
        if x in row:
            cols = list( enumerate(row) if len(row) != 0 else [] )
            cols.sort(key = lambda t: t[1])
            result.append((idx, cols[0][1]))
            rows.append((idx, len(row)))
    result.sort(key = lambda t: rows.index(t[1]))
    return result