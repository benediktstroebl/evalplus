
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
    res = []
    if not lst:
        return res
    if not lst[0]:
        return res
    for y, row in enumerate(lst):
        if row:
            ind = 0
            for xind, el in enumerate(row):
                if el == x:
                    ind = xind
                    break
            if ind > 0:
                res.append((y, ind))
    res.sort()
    tmp = []
    for y, ind in res:
        if not tmp:
            tmp = [(y, ind)]
        else:
            for t in tmp:
                if y == t[0]:
                    break
                elif y > t[0]:
                    tmp = [(y, ind)]
                    break
            else:
                tmp.append((y, ind))
    return sorted(tmp, key=lambda x: -x[1])
