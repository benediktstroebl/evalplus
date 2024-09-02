
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

    if lst == []:
        return []
    
    row_dict = dict()
    for row in lst:
        row_len = len(row)
        if row_len not in row_dict:
            row_dict[row_len] = [(lst.index(row), row.index(x))]
        else:
            row_dict[row_len].append((lst.index(row), row.index(x)))
    
    return_lst = []
    for row_len, coord_list in row_dict.items():
        for coord in coord_list:
            return_lst.append((coord[0], row_len - coord[1] - 1))
    
    return_lst.sort()
    return_lst = [coord for coord in return_lst if coord[0]!= coord[1]]
    return_lst.sort(key = lambda x: x[1], reverse = True)
    return return_lst

