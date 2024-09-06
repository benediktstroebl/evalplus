
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
    # Sorting rows by columns
    rows = sorted(lst, key=lambda x: x[1], reverse=True)
    row = rows[x]

    # Sorting columns by rows
    columns = [([y[0], y[1]] for y in row) if y[1] >= y[0] else []]
    row_sorted = [x[0] for x in rows]
    # Return the first column of the row
    return [row_sorted[j] for j, col in enumerate(columns) if j != 0]