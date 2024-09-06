def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        cols = len(row)
        if cols == x:
            result.append((i, cols))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1])
    return result