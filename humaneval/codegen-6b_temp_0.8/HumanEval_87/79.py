
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
    
    # remove all empty strings in list
    lst = [x for x in lst if x != []]
    
    # divide the list into 2 halves
    lst_1 = lst[:len(lst)//2]
    lst_2 = lst[len(lst)//2:]
    
    # sort the first half of the list
    lst_1.sort()
    
    # sort the second half of the list
    lst_2.sort(reverse = True)
    
    res = []
    
    # search for x in both halves
    for lst_1_item, lst_2_item in zip(lst_1, lst_2):
    
        # check if the left element of the list is x
        if lst_1_item == x:
            res.append((0, lst_2.index(lst_1_item)))
            
        # check if the right element of the list is x
        # if lst_2_item == x:
            # res.append((2, lst_1.index(lst_2_item)))
            
    return res
