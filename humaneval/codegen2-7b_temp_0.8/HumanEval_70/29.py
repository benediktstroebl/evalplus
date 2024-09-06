
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
        return lst
    if len(lst) < 2:
        return lst
    a = min(lst)
    b = max(lst)
    remain = [x for x in lst if x < a] + [x for x in lst if x >= a] + [x for x in lst if x > b]
    return strange_sort_list(remain) + [a] + [b] + strange_sort_list(remain)
