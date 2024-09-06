
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

    # 0. Imports
    from operator import itemgetter

    # 1. Check if given argument is a list
    # 2. If not, return an empty list
    if not isinstance(lst, list):
        return []
    # 3. Iterate over list
    # 4. If the element of the list is a list
    # 5. In that list, if there is an x
    # 6. Append tuple of (index, x_index) to list
    # 7. Return the list
    return list(map(itemgetter(0, 1), [(idx, el.index(x)) for idx, el in enumerate(lst) if x in el]))

