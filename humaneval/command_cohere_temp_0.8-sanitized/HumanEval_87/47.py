def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x == cols:
            result.append((idx, cols))
        elif x in row:
            result.append((idx, cols))
        idx += 1
    result.sort(key = lambda x: (x[0], -x[1]))
    return result