def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        row_with_x = []
        for j, col in enumerate(row):
            if col == x:
                row_with_x.append((i, j))
        result.extend(sorted(row_with_x, key=lambda x: (x[0] * 100000000 + x[1])))
    return result