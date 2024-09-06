def get_row(lst, x):
    res = []
    for row in lst:
        row_len = len(row)
        for j, col in enumerate(row):
            if col == x:
                res.append((row_len-1, row_len-j-1))
    res.sort(key=lambda x: (x[0], x[1]))
    return res