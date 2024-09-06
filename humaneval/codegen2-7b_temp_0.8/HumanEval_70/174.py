
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
    return_list = []
    lst_copy = lst[:]
    while len(lst_copy) > 0:
        minimum = min(lst_copy)
        return_list.append(minimum)
        lst_copy.remove(minimum)
        maximum = max(lst_copy)
        return_list.append(maximum)
        lst_copy.remove(maximum)
    return return_
