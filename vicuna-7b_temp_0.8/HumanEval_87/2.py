
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
    # Sorting rows
    row = sorted((lst[i] for i in range(len(lst))), key=lambda x: x[0])
    
    # Sorting columns
    col = sorted((lst[i][j] for i in range(len(lst)) for j in range(lst[i].count(1))), key=lambda x: x[1])
    
    # Finding coordinates of the row
    row_coord = [tuple(sorted((lst[i].count(j) for j in range(lst[i].count(1))), key=lambda x: x[1])) for i in range(len(lst))]
    
    # Returning the coordinates of the row
    return [(row_coord.index(c), j) for j, c in enumerate(col)]