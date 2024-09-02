
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
    # _row_in_lst = lambda row, lst: [i for i, row_i in enumerate(lst) if row in row_i]
    _row_in_lst = lambda row, lst: [i for i, row_i in enumerate(lst) if row in row_i]
    _row_coordinates = lambda row, lst, x: [(row, len(lst[row]) - i - 1) for i in range(len(lst[row])) if lst[row][i] == x]
    return sorted([(i, c) for row in _row_in_lst(x, lst) for i in range(len(lst)) for c in _row_coordinates(i, lst, x)])
