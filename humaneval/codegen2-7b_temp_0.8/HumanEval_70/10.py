
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
    low, max_, n = min(lst), max(lst), len(lst)
    for i in range(n-1):
        if max_ <= lst[i]:
            max_ = lst[i]
        lst[i] = max_
        max_ = low
    lst.reverse()
    return l
