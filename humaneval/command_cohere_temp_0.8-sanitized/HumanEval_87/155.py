def get_row(lst, x):
    res = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x:
            res.append((idx, len(row_x)))
            res.sort(key=lambda x: (x[0], -x[1]))
    return res