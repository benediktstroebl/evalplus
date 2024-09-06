
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
    rows = [lst[0]]
    for i in range(1, len(lst)):
        row = lst[i]
        if row:
            rows.append(row)
    row = rows[0]
    for i in range(1, len(rows)):
        row = rows[i]
        rows.remove(row)
        for j in range(len(row)):
            for k in range(len(row[0])):
                x = row[j][k]
                if x == x:
                    if x < x:
                        break
                    else:
                        break
                else:
                    if x < x:
                        break
                yield row[j], x