
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
    if len(lst) <= 1:
        return lst
    min_value = lst[0]
    max_value = lst[0]
    for i in range(len(lst)-1):
        if lst[i] > max_value:
            max_value = lst[i]
        if lst[i] < min_value:
            min_value = lst[i]
    return [min_value, max_value] + strange_sort_list(lst[1:])
