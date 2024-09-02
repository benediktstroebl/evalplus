
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
    my_list = []
    if len(lst) == 1:
        return lst
    elif len(lst) == 0:
        return my_list
    else:
        min_value = min(lst)
        max_value = max(lst)
        my_list.append(min_value)
        while max_value in lst:
            lst.remove(max_value)
            my_list.append(max_value)
        for i in lst:
            my_list.append(i)
    return my_list
