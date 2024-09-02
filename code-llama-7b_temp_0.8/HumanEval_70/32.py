
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
        return []

    new_lst = lst.copy()
    new_lst.sort()
    i = 0
    new_lst[i] = min(lst)

    for x in lst:
        if x != new_lst[i]:
            lst.remove(x)
            lst.append(x)

    return lst
