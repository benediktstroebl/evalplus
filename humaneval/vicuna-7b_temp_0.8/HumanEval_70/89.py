
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
    # check for empty list
    if not lst:
        return []

    # find the minimum value
    min_val = lst[0]
    for val in lst[1:]:
        if val < min_val:
            min_val = val

    # find the maximum of the remaining values
    max_val = lst[0]
    for val in lst[1:]:
        if val > max_val:
            max_val = val

    # sort the list in strange order
    return sorted([min_val, max_val, lst[0]]) + [lst[1:]]
