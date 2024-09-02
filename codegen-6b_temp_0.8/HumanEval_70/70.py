
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
    sorted_lst = []
    while lst:
        max_int = max(lst)
        sorted_lst.append(max_int)
        lst.remove(max_int)
        if lst:
            min_int = min(lst)
            sorted_lst.append(min_int)
            lst.remove(min_int)
    return sorted_lst

