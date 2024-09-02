
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
    row = lst
    row_index = 0
    col_index = 0
    x = x
    while x != -1:
        if x in row:
            row_index = row.index(x)
            col_index += 1
            if col_index == 1:
                yield (row_index, x)
                row_index = 0
                col_index = 1
        x = row.pop(row_index)
        row_index += 1
        if row_index == len(row):
            break
        if row_index == 0:
            row_index = 0
            col_index = 1
    if row:
        yield (row_index, x)
