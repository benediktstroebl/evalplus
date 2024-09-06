def get_row(lst, x):
    result = []
    rows = []
    for row in lst:
        if x in row:
            cols = len(row)
            result.append((len(rows), cols))
            rows.append(row)
    if x not in rows:
        return []
    result.sort(key=lambda x: (x[0], -x[1]))
    return result