
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
    if len(lst) == 1:
        return [lst[0]]
    elif len(lst) == 2:
        return sorted(lst)

    odds, evens = [], []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return strange_sort_list(odds) + strange_sort_list(evens)
