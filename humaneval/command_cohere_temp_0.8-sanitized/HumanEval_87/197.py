def get_row(lst, x):
    result = []
    for row in lst:
        cols = len(row)
        if x == cols:
            result.append((len(lst) - row.index(True), cols))
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result