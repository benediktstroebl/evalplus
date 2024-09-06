def get_row(lst, x):
    out = []
    for i, row in enumerate(lst):
        if x in row:
            out.append((i, row.index(x)))
    return sorted(out, key=lambda x: x[0])