
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
    lst = lst[0]
    row = x
    coord_lst = [(row, 0)]
    sorted_lst = []
    
    for row in lst:
        col = 0
        coord_lst.append((row, col))
        sorted_lst.append((row, col))
        for i in range(len(lst)):
            if row == i and col != 0:
                row -= 1
                col -= 1
            elif row != i:
                col = 0
                if row > i:
                    row += 1
                elif row < i:
                    col += 1
                if row != i:
                    coord_lst.append((row, col))
        coord_lst = sorted(coord_lst, key=lambda k: k[1])
        sorted_lst = sorted(sorted_lst, key=lambda k: k[1])
    
    return sorted_lst
