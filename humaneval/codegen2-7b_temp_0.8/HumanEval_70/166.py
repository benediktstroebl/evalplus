
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
    sorted_lst = []
    if not lst:
        return sorted_lst
    minimum_value = min(lst)
    for i in range(len(lst)):
        if lst[i] > minimum_value:
            sorted_lst.append(lst[i])
            minimum_value = min(lst[i + 1:])
    sorted_lst += lst[len(lst) - 1:]
    return sorted_lst



