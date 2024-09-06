def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x:
            result.append((len(lst) - row.index(row_x[0]) - 1, len(row_x)))
    return sorted(result, key=lambda x: (x[0], -x[1]))