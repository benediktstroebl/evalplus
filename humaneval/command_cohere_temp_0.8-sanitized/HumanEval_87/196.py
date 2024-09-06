def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if cols == x:
            result.append((idx, cols))
            result.sort(key = lambda x: x[1])
        idx += 1
    result.sort(key = lambda x: x[0])
    return result