def get_row(lst, x):
    result = []
    for row in lst:
        if x in row:
            result.append((row.index(x), len(row)))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result