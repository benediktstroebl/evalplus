def get_row(lst, x):
    result = []
    rows = []
    r, c = 0, 0
    for row in lst:
        if x in row: 
            col = row.index(x)
            result.append((r, c))
            result.sort(key=lambda x: (x[1], x[0]))
            c += 1
        else: 
            c = 0
        if not c: 
            r += 1
            c, rows = 0, []
    return result + sorted(rows)