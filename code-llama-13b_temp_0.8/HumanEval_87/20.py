
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
    if len(lst) == 0:
        return []
    lst2 = lst
    lst3 = []
    for i in range(len(lst2)):
        for j in range(len(lst2[i])):
            if lst2[i][j] == x:
                lst3.append((i, j))
    lst3.sort()
    for i in range(len(lst3)):
        lst3[i] = (lst3[i][0], lst3[i][1]-len(lst2[lst3[i][0]]))
    for i in range(len(lst3)):
        lst3[i] = (lst3[i][0], lst3[i][1]-lst3[i][0]-1)
    return lst3

