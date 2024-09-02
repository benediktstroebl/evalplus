
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
    lst = sorted(lst, key=lambda x: x[0])
    row = [lst.index(x) for x in lst if x[0] == x[0]]
    x_indices = [lst.index(x) for x in lst if x[0] == x[0]]
    if not row:
        return []
    for i in range(1, len(row)):
        y = lst[row[i]]
        y = [y[0]]
        for j in range(len(y)):
            y[j] = y[j] + 1
        if y[0] == y[-1]:
            y.append(0)
        else:
            y.insert(0, 0)
        x_indices = [x for x in x_indices if x == y.index(y[-1])]
    return [(row[i], y) for i, y in enumerate(zip(*x_indices))]