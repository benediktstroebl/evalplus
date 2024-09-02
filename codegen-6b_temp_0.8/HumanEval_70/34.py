
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

    min_num = lst[0]
    max_num = lst[-1]
    middle = len(lst) // 2
    first = lst[:middle]
    second = lst[middle:]

    return strange_sort_list(first) + \
        [min_num] + strange_sort_list(second) + \
        [max_num]

