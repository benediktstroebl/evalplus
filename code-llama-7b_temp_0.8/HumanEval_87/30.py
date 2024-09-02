
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
    # single list
    # nested list
    # reverse to get correct (row, col)
    # check if x in list
    # if not, return []
    # otherwise, get the row and the column
    # sort row ascending order
    # sort column descending order
    # return [ (row, col), (row, col) ]
    
    # find the row first
    
    # single list
    if not lst:
        return []
    
    # nested list
    if len(lst) < 2:
        for row in lst:
            if x in row:
                return [(0, row.index(x))]
    else:
        for i in range(len(lst)):
            if x in lst[i]:
                return [(i, lst[i].index(x))]
