
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
    n = len(lst)
    res = []
    res1 = sorted(lst)
    if n == 0:
        return res
    res.append(res1[0])
    i = 0
    while i < n - 1:
        res.append(res1[n - 1 - i])
        i += 1
    return res

