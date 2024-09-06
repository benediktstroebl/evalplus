def get_row(lst, x):
    res = []
    for i, row in enumerate(lst):
        col = [y for y in row if y == x]
        if col:
            res.append((i, len(col)))
    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[1], reverse=True)
    return res