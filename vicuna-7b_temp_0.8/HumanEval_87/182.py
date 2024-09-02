
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
    if not lst:
        return []
    
    if not x in lst:
        return []
    
    row_coords = [(lst.index(x), i) for i, x in enumerate(lst[1:])]
    row_coords.sort(key=lambda x: (x[0], -x[1]))
    
    coord = [(0, x)]
    for i, (r, c) in enumerate(row_coords):
        coord.append((i+1, c))
        if coord[i+1][1] < coord[i+2][1]:
            coord[i:].sort((lambda x, y: cmp(x[1], y), reverse=True))
    return coord