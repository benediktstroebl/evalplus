
def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    """
    row_lst = lst[0]
    row_lst_copy = copy.copy(row_lst)
    if not row_lst:
        return []
    if not row_lst[-1]:
        return [row_lst[-1]]
    sorted_lst = sorted(row_lst)
    rows = sorted_lst[:-1]
    for row in rows:
        col_lst = row
        col_lst_copy = copy.copy(col_lst)
        if not col_lst:
            continue
        if not col_lst[-1]:
            continue
        sorted_col = sorted(col_lst[-1], reverse=True)
        return [(x, y) for x, y in zip(rows, sorted_col)]
