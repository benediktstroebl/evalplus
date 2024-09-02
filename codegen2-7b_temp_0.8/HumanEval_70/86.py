
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
    strange_order = []
    n = len(lst)

    for i in range(n):
        if i+1 == n:
            strange_order.extend(lst)
        else:
            min_value = min(lst[i:])
            strange_order.extend(lst[i:][lst[i:] >= min_value])
            lst[i:] = lst[i:] - min_value

    return strange_order
