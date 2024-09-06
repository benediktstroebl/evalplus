
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
    # check for empty list
    if len(lst) == 0:
        return []
    
    # create dict
    d = {}
    
    # loop over lst
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                if i not in d:
                    d[i] = []
                d[i].append((j, lst[i][j]))

    # convert dict to list
    lst2 = []
    for k, v in d.items():
        for i in range(len(v)):
            lst2.append((k, v[i]))

    # sort by row
    lst2.sort(key=lambda x: x[0])
    
    # sort row by column
    for i in range(len(lst2)):
        if len(lst2[i]) > 1:
            lst2[i] = list(lst2[i])
            lst2[i].sort(key=lambda x: x[0], reverse=True)
            lst2[i] = tuple(lst2[i])
            
    return lst2
