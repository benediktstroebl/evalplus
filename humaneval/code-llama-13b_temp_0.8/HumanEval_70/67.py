
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
    lst_sorted = sorted(lst)
    result = [lst_sorted.pop(0)]
    while lst_sorted:
        result.append(lst_sorted.pop(-1))
        if lst_sorted:
            result.append(lst_sorted.pop(0))
    return result

