def get_row(lst, x):
    res = []
    for i, row in enumerate(lst):
        col = 0
        for j in range(len(row)):
            if row[j] == x:
                res.append((i, col))
                col += 1
            else:
                col = 0
        if col > 0:
            res.append((i, col))
    res.sort(key=lambda x: x[0])
    res.sort(key=lambda x: x[1], reverse=True)
    return res