
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
    min = lst[0]
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < min:
            min = lst[i]
            min_index = i
    tmp = lst[min_index]
    lst[min_index] = lst[0]
    lst[0] = tmp
    strange_sort_list(lst[1:])
    return l
