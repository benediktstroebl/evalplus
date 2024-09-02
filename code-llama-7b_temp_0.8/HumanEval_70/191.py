
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
    result = []
    while lst:
        min_value = min(lst)
        result.append(min_value)
        lst.remove(min_value)
        if not lst:
            return result
        max_value = max(lst)
        result.append(max_value)
        lst.remove(max_value)
        if not lst:
            return result
        min_value = min(lst)
        result.append(min_value)
        lst.remove(min_value)
        if not lst:
            return result
        max_value = max(lst)
        result.append(max_value)
        lst.remove(max_value)
    return result
