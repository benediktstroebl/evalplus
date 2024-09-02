
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

    if len(lst) == 1:
        return lst

    if len(lst) == 0:
        return lst

    new_lst = []
    while len(lst) > 0:
        min_value = min(lst)
        max_value = max(lst)
        new_lst.append(min_value)
        lst.remove(min_value)
        if lst:
            lst.remove(max_value)
            new_lst.append(max_value)

    return new_lst

