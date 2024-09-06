
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
    for i in range(len(lst)):
        # Find minimum value
        min_value = min(lst)
        # Remove minimum value from list
        lst.remove(min_value)
        # Find maximum value
        max_value = max(lst)
        # Remove maximum value from list
        lst.remove(max_value)
        # Append maximum value to result
        result.append(max_value)
        # Append minimum value to result
        result.append(min_value)
        # Append minimum value to lst
        lst.append(min_value)
        # Append maximum value to lst
        lst.append(max_value)
    return result
