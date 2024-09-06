
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
    lst = sorted(lst)
    min_val = lst[0]
    lst[0] = min_val
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > 1:
            lst[i] -= 1
    return lst

