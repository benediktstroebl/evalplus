
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
    min_value = min(lst)
    new_list = [min_value]
    while lst:
        lst.remove(min_value)
        if lst:
            max_value = max(lst)
            new_list.append(max_value)
            lst.remove(max_value)
            if lst:
                min_value = min(lst)
                new_list.append(min_value)
                lst.remove(min_value)
    return new_list

