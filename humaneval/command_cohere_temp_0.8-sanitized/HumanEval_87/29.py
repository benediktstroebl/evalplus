def get_row(lst, x):
    result = []
    rows = []
    r, c = 0, 0
    for row in lst:
        if x in row: 
            cols = len(row)
            result.append((r, cols))
            rows.append(r)
            r += 1
            c = max(c, cols)
    result.sort(key=lambda x: (x[0], -x[1]))
    rows.sort(key=lambda x: x[1])
    return [(row, cols) for row, cols in result if row in rows and cols == c]