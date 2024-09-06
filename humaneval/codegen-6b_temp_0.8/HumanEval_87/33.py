
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
    
    lst_m = lst
    
    if lst == []:
        return []
    elif lst_m[0] == []:
        lst_m[0] = lst[1]
    elif lst_m[0][0] == lst[1][0]:
        lst_m[0] = lst[0] + lst[1]
        lst_m.remove(lst[1])
    elif lst_m[-1][-1] == lst[1][-1]:
        lst_m[-1] = lst[0] + lst[1]
        lst_m.remove(lst[1])
    elif lst_m[-1][-1] < lst[1][-1]:
        lst_m[-1] = lst[0] + lst[1]
        lst_m.remove(lst[1])
    else:
        lst_m[0] = lst[0] + lst[1]
        lst_m.remove(lst[1])
    
    # Sort by rows
    lst_copy = lst_m[:]
    lst_copy.sort()
    
    # Sort by cols
    lst_copy_r = []
    for i in lst_copy:
        lst_copy_r.append(list(reversed(sorted(i))))
    lst_copy_r.sort()
    lst_copy_r = [list(reversed(i)) for i in lst_copy_r]
    
    return [(0, x-1)] + [tuple(c) for c in zip(lst_copy_r, lst_copy)] + [(len(lst_copy)-1, x-1)]

