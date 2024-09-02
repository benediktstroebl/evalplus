
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
    strange_sort = []
    min_value = min(lst)
    for i in lst:
        if i < min_value:
            strange_sort.append(min_value)
            min_value += 1
        else:
            strange_sort.append(i)
    return strange_sort
