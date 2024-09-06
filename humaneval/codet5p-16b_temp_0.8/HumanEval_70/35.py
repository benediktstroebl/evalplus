
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

    ret = []
    if len(lst) == 0:
        return []
    min_index = 0
    min_val = lst[0]
    for i, val in enumerate(lst):
        if val < min_val:
            min_val = val
            min_index = i

    ret.append(lst.pop(min_index))
    for i in sorted(lst, reverse=True):
        ret.append(i)
    return ret
