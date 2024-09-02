
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

    lst.sort()
    lst_1 = lst[:]
    lst_2 = lst[:]
    result = []
    while len(lst_1) > 0 or len(lst_2) > 0:
        min_val = min(lst_1)
        result.append(min_val)
        lst_1.remove(min_val)
        if len(lst_1) > 0:
            max_val = max(lst_2)
            lst_2.remove(max_val)
            result.append(max_val)
    return result
