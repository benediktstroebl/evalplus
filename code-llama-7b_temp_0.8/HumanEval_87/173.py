
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
    def inner_find_index(lst, x):
        if len(lst) == 0:
            return -1
        elif len(lst) == 1:
            return lst[0].index(x)
        else:
            middle = len(lst)//2
            if lst[middle] == x:
                return middle
            elif lst[middle] < x:
                return inner_find_index(lst[middle:], x)
            else:
                return inner_find_index(lst[:middle], x)
    
    def inner_get_coord(lst, x):
        if len(lst) == 0:
            return []
        elif len(lst) == 1:
            return [(0, lst[0].index(x))]
        else:
            middle = len(lst)//2
            if lst[middle][0] == x:
                return [(middle, inner_find_index(lst[middle], x))]
            elif lst[middle][0] < x:
                return inner_get_coord(lst[middle:], x)
            else:
                return inner_get_coord(lst[:middle], x)
    
    def inner_get_row(lst, x):
        if len(lst) == 0:
            return []
        elif len(lst) == 1:
            return [(0, inner_find_index(lst[0], x))]
        else:
            middle = len(lst)//2
            if lst[middle][0] == x:
                return inner_get_coord(lst[middle], x)
            elif lst[middle][0] < x:
                return inner_get_coord(lst[middle:], x)
            else:
                return inner_get_coord(lst[:middle], x)
            
    if x in lst:
        return sorted(inner_get_row(lst, x))
    else:
        return []
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
