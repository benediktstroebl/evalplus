
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
    if len(lst) < 2:
        return lst
    else:
        first = lst[0]
        last = lst[-1]
        mid = int((first + last) / 2)
        mid_index = lst.index(mid)
        return strange_sort_list(lst[:mid_index]) + [mid] + strange_sort_list(lst[mid_index+1:])


