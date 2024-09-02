
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
    #my_lst=[]
    # for i in lst:
    #     for j in i:
    #         my_lst.append(j)
    #     if x in my_lst:
    #         print(my_lst.index(x),my_lst.index(x))
    #         my_lst.remove(x)
    
    # my_lst=[]
    # for i in lst:
    #     for j in i:
    #         my_lst.append(j)
    #     print(i)
    #     if x in i:
    #         print(i.index(x),my_lst.index(x))
    #         my_lst.remove(x)
    #     else:
    #         print("Element not found")
    # # print(lst)
    # # print(my_lst)

    # return [
    #     (i, lst[i].index(x))
    #     for i in range(len(lst))
    #     for j in range(len(lst[i]))
    #     if lst[i][j] == x
    # ]

    # print(lst)
    # print(x)
    # return [(i, lst[i].index(x)) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]

    # return [
    #     (i, lst[i].index(x))
    #     for i in range(len(lst))
    #     for j in range(len(lst[i]))
    #     if lst[i][j] == x
    # ]

    # lst2 = []
    # for l in lst:
    #     lst2.extend(l)

    # return [(i, lst2.index(x)) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]

    return [
        (i, lst[i].index(x)) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j]
