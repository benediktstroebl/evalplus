def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    cols = []
    for row in lst:
        cols.append(len(row))
    for i, r_length in enumerate(rows):
        if r_length > x:
            break
        j = cols[i] - 1
        while j >= 0 and rows[i] >= x:
            result.append((i, j))
            j -= 1
    result.sort(key=lambda x: (x[1], x[0]))
    return result