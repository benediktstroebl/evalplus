
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
    if len(lst) % 2 == 1:
        res = [lst[0]]
        lst.remove(lst[0])
    else:
        res = []
    while lst:
        res += [min(lst), max(lst)]
        lst.remove(max(lst))
        lst.remove(min(lst))
    return res

