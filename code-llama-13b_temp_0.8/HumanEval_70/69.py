
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    # # 1) Using set()
    # new_lst = []
    # while len(lst) != 0:
    #     new_lst += [min(lst)]
    #     lst.remove(min(lst))

    # while len(lst) != 0:
    #     new_lst += [max(lst)]
    #     lst.remove(max(lst))

    # return new_lst

    # # 2) Without set()
    # new_lst = []
    # lst_cpy = lst.copy()
    # while len(lst) != 0:
    #     new_lst += [lst_cpy[lst.index(min(lst_cpy))]]
    #     lst.remove(min(lst))
    #     lst_cpy.remove(min(lst_cpy))

    # while len(lst) != 0:
    #     new_lst += [lst_cpy[lst.index(max(lst_cpy))]]
    #     lst.remove(max(lst))
    #     lst_cpy.remove(max(lst_cpy))

    # return new_lst

    # 3) Using more set()
    new_lst = []
    lst_cpy = lst.copy()
    while len(lst_cpy) != 0:
        new_lst += [lst_cpy[lst_cpy.index(min(lst_cpy))]]
        lst_cpy.remove(min(lst_cpy))
        lst.remove(min(lst))

    while len(lst_cpy) != 0:
        new_lst += [lst_cpy[lst_cpy.index(max(lst_cpy))]]
        lst_cpy.remove(max(lst_cpy))
        lst.remove(max(lst))

    return new_lst

