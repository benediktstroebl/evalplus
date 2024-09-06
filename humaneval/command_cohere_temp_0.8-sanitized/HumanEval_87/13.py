def get_row(lst, x):
    result = []
    rows = []
    for idx, row in enumerate(lst):
        if x in row:
            result.append((idx, len(row)))
            rows.append(row)
    result.sort(key=lambda x: (x[0], -x[1]))
    return [tuple(row) for row in result if row[0] in rows]