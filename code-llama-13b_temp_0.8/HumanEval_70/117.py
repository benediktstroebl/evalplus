
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

    lst_copy = lst.copy()
    lst_len = len(lst)
    result = []
    for i in range(lst_len):
        minimum = min(lst)
        maximum = max(lst)
        lst.remove(maximum)
        result.append(maximum)
        if i % 2:
            result.append(minimum)
        lst.remove(minimum)

    return result

