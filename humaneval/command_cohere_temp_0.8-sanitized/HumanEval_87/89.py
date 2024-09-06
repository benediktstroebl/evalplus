def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        cols = len(row)
        if cols > x: 
            continue
        j = bisect.bisect_left(row, x)
        result.append((i, j))
    result.sort(key=lambda x: (x[1], x[0]))
    return result