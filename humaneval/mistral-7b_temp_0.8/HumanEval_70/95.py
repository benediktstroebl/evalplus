
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
    result = []
    cur_min = min(lst)
    cur_max = max(lst)
    result.append(cur_min)
    lst.remove(cur_min)
    result.append(cur_max)
    lst.remove(cur_max)
    while lst:
        cur_min = min(lst)
        lst.remove(cur_min)
        result.append(cur_min)
        cur_max = max(lst)
        lst.remove(cur_max)
        result.append(cur_max)
    return result
