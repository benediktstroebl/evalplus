
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

    length_lst = len(lst)
    result = []
    for i in range(length_lst):
        if not lst:
            break;
        result.append(lst[0])
        lst.remove(lst[0])
        if i < length_lst - 1:
            result.append(max(lst))
            lst.remove(max(lst))
        if i < length_lst - 2:
            result.append(min(lst))
            lst.remove(min(lst))
    return result
