def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x < cols:
            result.append((row, x))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result