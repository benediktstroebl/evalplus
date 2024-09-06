
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

    lst_len = len(lst)
    if lst_len == 0:
        return lst

    result = []
    result.append(min(lst))
    while lst_len > 1:
        lst.remove(min(lst))
        lst_len -= 1
        result.append(max(lst))
        lst.remove(max(lst))
        lst_len -= 1
        result.append(min(lst))

    return result

