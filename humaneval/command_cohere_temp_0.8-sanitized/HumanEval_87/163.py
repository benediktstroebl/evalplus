def get_row(lst, x):
    out = []
    for i, row in enumerate(lst):
        col = next((j for j, val in enumerate(row) if val == x), -1)
        out.append((i, col))
    return sorted(out, key=lambda x: (x[0], -x[1]))