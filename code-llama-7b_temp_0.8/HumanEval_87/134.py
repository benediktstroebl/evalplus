
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
    # My version
    def get_row_inner(lst, x, row_index, result):
        lst_len = len(lst)
        if lst_len == 0:
            return result
        if x in lst[row_index]:
            result.append((row_index, lst[row_index].index(x)))
        result = get_row_inner(lst, x, row_index + 1, result)
        return result
    result = []
    return sorted(get_row_inner(lst, x, 0, result), key=lambda x: (x[0], -x[1]))


    # My version 2
    # result = []
    # def get_row_inner(lst, x, row_index, result):
    #     lst_len = len(lst)
    #     if lst_len == 0:
    #         return result
    #     if x in lst[row_index]:
    #         result.append((row_index, lst[row_index].index(x)))
    #     return get_row_inner(lst, x, row_index + 1, result)
    # return sorted(get_row_inner(lst, x, 0, result), key=lambda x: (x[0], -x[1]))

    # Other versions
    # ...
