def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if cols == x:
            result.append((len(lst) - row[::-1].index(row), cols))
    return sorted(result, key=lambda x: (x[0], -x[1]))