def get_row(lst, x):
    out = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                out.append((i, j))
    out.sort(key=lambda x: (x[0], -x[1]))
    return out