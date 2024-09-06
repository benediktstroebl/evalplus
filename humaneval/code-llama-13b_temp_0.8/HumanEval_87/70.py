
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
    # if not lst:
    #     return []
    # row_dict = {}
    # for idx, sublst in enumerate(lst):
    #     if x in sublst:
    #         if idx in row_dict:
    #             row_dict[idx].append(sublst.index(x))
    #         else:
    #             row_dict[idx] = [sublst.index(x)]
    # row_dict = {key: sorted(value, reverse=True) for key, value in row_dict.items()}
    # return [item for value in row_dict.values() for item in [(key, value) for value in value]]

    if not lst:
        return []
    return sorted([(i, x.index(y)) for i,x in enumerate(lst) for y in x if y==x])
