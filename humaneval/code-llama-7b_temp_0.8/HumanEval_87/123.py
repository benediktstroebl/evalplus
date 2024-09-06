
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

    # a good error message comes with the type of the error
    if not lst:
        return []
    # return x in lst if x is in lst[0] else return x in lst[1:]
    # a single for loop is fine, we just need to check if it is in the first sublist,
    # if not, then we check if it is in the next sublist, etc.
    # in the end, we return a list of tuples, since that is what the problem wants
    for i, sublist in enumerate(lst):
        if x in sublist:
            return [(i, sublist.index(x))]
    return []
