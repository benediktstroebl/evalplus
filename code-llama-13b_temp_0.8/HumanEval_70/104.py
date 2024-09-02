
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
    new_list = lst.copy()

    while new_list:
        min_val = min(new_list)
        result.append(min_val)
        new_list.remove(min_val)

        max_val = max(new_list)
        result.append(max_val)
        new_list.remove(max_val)

    return result

