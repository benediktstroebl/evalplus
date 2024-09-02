
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
    res = []
    if not lst:
        return []
    res.append(min(lst))
    for i in range(len(lst)):
        if lst[i] == min(lst):
            continue
        res.append(min(lst))
        lst.remove(min(lst))
        lst.append(min(lst))
    res.extend(sorted(lst, reverse=True))
    return
