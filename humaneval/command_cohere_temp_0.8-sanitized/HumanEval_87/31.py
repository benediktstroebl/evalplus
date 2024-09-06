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
    result.sort(key = lambda x:-x[1])
    result.sort(key = lambda x:-rows.index(x[0]))
    return result