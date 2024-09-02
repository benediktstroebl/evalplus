
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
    elif lst[0] == min(lst):
        return lst[1:len(lst)-1] + [lst[0]] + lst[len(lst)-1:]
    else:
        return strange_sort_list(lst[1:]) + [lst[0]] + strange_sort_list(lst[len(lst)-1:])
