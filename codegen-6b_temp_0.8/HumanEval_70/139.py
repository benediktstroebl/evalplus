
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

    if len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        else:
            return lst

    if len(lst) > 3:
        return lst

    lst = sorted(lst)

    if max(lst[0], lst[-1]) == lst[0]:
        return lst[::-1]
    elif max(lst[0], lst[-1]) == lst[-1]:
        return lst

    return [lst[0], lst[-1]]
