def get_row(lst, x):
    result = []
    for row in lst:
        row_x = [col for col in row if col == x]
        if row_x: 
            col_sort = sorted(row_x)
            result.append((len(lst) - row.index(col_sort[0]) - 1, len(col_sort)))
    return result