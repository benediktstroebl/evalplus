
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
    if len(lst) == 0:
        return lst
    smallest, largest = min(lst), max(lst)
    for val in lst:
        if smallest == val:
            smallest, lst[lst.index(val)] = smallest - 1, lst[lst.index(val) - 1]
        elif largest == val:
            largest, lst[lst.index(val)] = lst[lst.index(val) + 1], largest - 1
    return lst
