
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
    if len(lst) <= 1:
        return lst
    min_value = min(lst)
    max_value = max(lst)
    result = [min_value, max_value]
    list_copy = lst.copy()
    list_copy.remove(min_value)
    list_copy.remove(max_value)
    if len(list_copy) % 2 == 0:
        result.extend([min_value, max_value])
        result.extend(sorted(list_copy))
    else:
        result.append(max_value)
        result.extend(sorted(list_copy))
        result.append(min_value)
    return result
