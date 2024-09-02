
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
    elif len(lst) == 1:
        return [lst[0]]
    else:
        # Determine maximum value
        max_val = lst[0]
        for val in lst[1:]:
            if val > max_val:
                max_val = val
        # Determine min and max
        min_val = lst[0]
        for val in lst[1:]:
            if val < min_val:
                min_val = val
        # Sort the list
        return [max_val, min_val, sorted(lst[1:], reverse=True)[0]]