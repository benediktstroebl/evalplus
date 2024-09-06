
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
    # not good, O(NMlogN)
    # rows = [(x1, y1) for x1, row in enumerate(lst) for y1, x2 in enumerate(row) if x == x2]
    # return sorted(rows, key = lambda row: (row[0], -row[1]))
    # better, O(NM)
    # return sorted([(x1, y1) for x1, row in enumerate(lst) for y1, x2 in enumerate(row) if x == x2], key = lambda row: (row[0], -row[1]))
    # best, O(NM)
    result = []
    for x1, row in enumerate(lst):
        x1 = x1 + 1
        if x in row:
            x2 = row.index(x)
            result.append((x1, x2))
    return sorted(result, key = lambda row: (row[0], -row[1]))
