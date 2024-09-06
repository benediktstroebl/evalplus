def get_row(lst, x):
    result = []
    rows = []
    for sub_list in lst:
        if x in sub_list:
            row_num = sub_list.index(x) + 1
            cols = len(sub_list)
            result.append((row_num, cols))
            rows.append(row_num)
    result.sort(key=lambda x: (x[0], -x[1]))
    rows.sort(key=lambda x: x[0])
    return [(row, cols) for row, cols in result if row == rows[0]]