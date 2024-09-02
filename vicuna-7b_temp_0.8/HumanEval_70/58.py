
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
    res = [min(lst)]
    for i in range(1, n):
        a = min(lst[i-1], lst[i])
        res.append(lst.count(a) % 2 == 0 and a or max(lst[i-1], lst[i]))
    return res
