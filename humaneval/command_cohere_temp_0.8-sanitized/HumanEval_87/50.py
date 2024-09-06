def get_row(lst, x):
    result = []
    rows = []
    for idx, row in enumerate(lst):
        if x in row:
            result.append((idx, len(row)))
            rows.append(row)
    result.sort(key=lambda x: (x[0], -x[1]))
    rows = sorted(rows, key=lambda x: x.index(x))
    return [(idx, len(row)) for idx, row in zip(rows, result)]