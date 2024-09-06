
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
    row_coords = [(y, x) for x, y in lst]
    row_coords.sort(key=lambda x: x[0])
    row_coords.sort(key=lambda x: x[1])
    return [row for row in row_coords if row[0] == x]

lst = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1],
    [7, 8, 9, 10, 11, 12],
    [7, 8, 9, 10, 7, 12],
    [7, 8, 9, 10, 11, 8],
    [13, 14, 15, 16, 17, 18],
    [13, 14, 15, 16, 17, 13],
    [13, 14, 15, 16, 18, 14],
    [18, 19, 20, 21, 22, 23],
    [18, 19, 20, 21, 22, 18],
    [18, 19, 20, 21, 23, 20],
    [23, 24, 25, 26, 27, 28],
    [23, 24, 25, 26, 27, 23],
    [23, 24, 25, 28, 24, 26],
    [23, 24, 25, 27, 25, 23],
    [23, 24, 25, 27, 27, 24],
    [23, 24, 25, 28, 2
