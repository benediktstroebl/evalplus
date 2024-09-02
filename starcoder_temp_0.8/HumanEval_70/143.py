
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

    if lst == []:
        return lst

    lst_min = min(lst)
    # temp_lst = lst.copy()
    # temp_lst.remove(lst_min)
    # if temp_lst == []:
    #     return [lst_min]
    # else:
    lst_max = max(lst)
    # temp_lst = lst.copy()
    # temp_lst.remove(lst_max)
    # if temp_lst == []:
    #     return [lst_max]
    # else:
    return [lst_min, lst_max] + [i for i in lst if i!= lst_max and i!= lst_min]
