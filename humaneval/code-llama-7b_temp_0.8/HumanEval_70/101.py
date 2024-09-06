
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
    if not lst:
        return []
    mx = lst[0]
    mn = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > mx:
            mx = lst[i]
        elif lst[i] < mn:
            mn = lst[i]
    return [mn, mx] + strange_sort_list(lst[2:])

