
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
    min_val = min(lst)
    max_val = max(lst)
    length = len(lst)
    while length > 0:
        result.append(max_val)
        result.append(min_val)
        length -= 2
        min_val = min(lst)
        max_val = max(lst)
    return result
