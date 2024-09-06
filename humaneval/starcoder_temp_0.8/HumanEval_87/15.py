
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
    lst_2d = []
    for i in lst:
        if type(i) is list:
            lst_2d.append(i)
    if lst_2d == []:
        return []
    out_list = []
    for i in range(len(lst_2d)):
        if x in lst_2d[i]:
            for j in range(len(lst_2d[i])):
                if lst_2d[i][j] == x:
                    out_list.append((i,j))
    out_list.sort(key=lambda x: x[0])
    out_list_2 = []
    for i in out_list:
        out_list_2.append((i[0], len(lst_2d[i[0]])-1-i[1]))
    out_list_2.sort(key=lambda x: x[0])
    return out_list_2
