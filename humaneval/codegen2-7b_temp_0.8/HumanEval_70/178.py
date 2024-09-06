
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
    n = len(lst)
    if n == 0:
        return []
    strange_sort = []
    minimum = lst[0]
    maximum = lst[0]
    for i in lst[1:]:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    strange_sort.extend([minimum] * (n-1))
    strange_sort.extend([maximum] * (n-1))
    return strange_sort

