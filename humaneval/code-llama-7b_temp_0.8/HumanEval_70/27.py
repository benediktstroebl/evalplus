
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
    if lst:
        min_value = min(lst)
        max_value = max(lst)
        result.append(min_value)
        result.append(max_value)
        result.extend(sorted(lst[:-2], reverse=True))
        return result
    return lst

