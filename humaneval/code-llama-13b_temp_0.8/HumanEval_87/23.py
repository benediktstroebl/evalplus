
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

    #print(lst)
    #print(lst[0])

    #lst_transpose = zip(*lst)

    #print(lst_transpose)

    #lst_transpose = list(lst_transpose)

    #print(lst_transpose)

    #lst_transpose_sorted = sorted(lst_transpose, reverse=True, key=lambda x:len(x))

    #print(lst_transpose_sorted)

    #lst_transpose_sorted = list(lst_transpose_sorted)

    #print(lst_transpose_sorted)

    #return sorted(
    #  [[i,lst_transpose_sorted[i].index(x)] for i in range(len(lst_transpose_sorted)) if x in lst_transpose_sorted[i]]
    #  , key=lambda x:x[0])

    # lst_transpose = list(zip(*lst))
    #
    # lst_transpose_sorted = sorted(lst_transpose, key=lambda x:len(x))
    #
    # return sorted(
    #   [[lst_transpose_sorted.index(x), x.index(value)] for x in lst_transpose_sorted for value in x if value == x]
    #   , key=lambda x:x[0])

    return sorted(
      [[i,lst[i].index(x)] for i in range(len(lst)) for x in lst[i] if x == x]
      , key=lambda x:x[0])

