
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
    if not lst:
        return []
    
    row_lst = []
    for row in lst:
        row_lst += [x for x in row]
    row_lst = sorted(row_lst, key=lambda x: x[0])
    
    coord_lst = [[0] * (len(row_lst[0]) + 1) for _ in range(len(lst))]
    for row in row_lst:
        for i, col in enumerate(coord_lst):
            coord_lst[i][i] = row.index(x) + 1
        coord_lst[i][-1] = row.index(x) + 1
        coord_lst[i].sort(key=lambda x: (-x[1], x[0]))
    return [tuple(coord) for coord in coord_lst]
