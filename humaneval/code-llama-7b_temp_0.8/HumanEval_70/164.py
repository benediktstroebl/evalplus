
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
    lst = lst.copy()
    while len(lst) > 0:
        lst.sort()
        res.append(lst.pop(0))
        lst.pop()
        lst.sort(reverse=True)
        res.append(lst.pop(0))
    return res

