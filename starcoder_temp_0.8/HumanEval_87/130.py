
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
    def get_row(lst, x, i, j):
        if j >= len(lst[0]):
            return [(i, j)]
        if lst[i][j] == x:
            return [(i, j)] + get_row(lst, x, i, j + 1)
        else:
            return get_row(lst, x, i, j + 1)

    return sorted(map(lambda x: (x[0], len(lst[x[0]]) - x[1] - 1),
                      filter(lambda x: lst[x[0]][len(lst[x[0]]) - x[1] - 1] == x[1],
                             map(lambda x: (x[0], len(lst[x[0]]) - x[1]),
                                 filter(lambda x: x[1]!= 0,
                                        map(lambda x: (x[0], len(lst[x[0]]) - x[1] - 1),
                                            enumerate(reduce(lambda a, b: a + b, lst))))))),
                  key=lambda x: (x[0], x[1]))
