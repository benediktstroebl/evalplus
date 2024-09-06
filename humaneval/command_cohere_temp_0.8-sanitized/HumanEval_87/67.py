def get_row(lst, x):
    result = []
    rows = [len(row) for row in lst]
    col_indices = [cols for row in lst for cols in enumerate(row)]
    for i, row_cols in enumerate(zip(rows, col_indices)):
        if x == row_cols[0]:
            result.append((i, row_cols[1]))
    result.sort()
    result.sort(key=lambda x: x[1])
    return result