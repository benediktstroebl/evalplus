
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

    if not lst: return []
    result = []
    min_index = 0
    while lst:
        min_index = find_min(lst)
        result.append(lst[min_index])
        lst.pop(min_index)
        max_index = find_max(lst)
        result.append(lst[max_index])
        lst.pop(max_index)
    return result
