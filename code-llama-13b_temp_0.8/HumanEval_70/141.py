
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

    result = []
    while lst:
        lst.sort()
        result.append(lst[0])
        del lst[0]
        if lst:
            lst.reverse()
            result.append(lst[0])
            del lst[0]
            if lst:
                lst.sort()
    return result

