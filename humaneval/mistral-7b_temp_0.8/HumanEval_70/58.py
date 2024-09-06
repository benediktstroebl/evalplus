
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

    while lst:
        min_int = min(lst)
        lst.remove(min_int)
        sorted_lst.append(min_int)

        if lst:
            max_int = max(lst)
            lst.remove(max_int)
            sorted_lst.append(max_int)

    return sorted_lst

