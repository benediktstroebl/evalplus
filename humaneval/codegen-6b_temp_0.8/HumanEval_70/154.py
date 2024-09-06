
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
    lst = lst or []
    lst = list(lst)
    lst.sort()
    i, j = 0, len(lst) - 1
    while i < j:
        mn, mx = lst[i], lst[j]
        if mn < mx:
            lst[i], lst[j] = mx, mn
            i += 1
        else:
            lst[i], lst[j] = mn, mx
            j -= 1
    return lst
