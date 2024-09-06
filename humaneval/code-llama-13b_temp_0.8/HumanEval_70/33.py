
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
        return lst

    result = []

    min_val = min(lst)
    max_val = max(lst)
    list_remain = lst.copy()

    while min_val or max_val:
        if min_val:
            result.append(min_val)
            list_remain.remove(min_val)

        if max_val:
            result.append(max_val)
            list_remain.remove(max_val)

        min_val = min(list_remain) if list_remain else None
        max_val = max(list_remain) if list_remain else None

    return result

