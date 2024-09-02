
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

    result = []
    if len(lst) == 0:
        return []
    result.append(lst[0])
    for i in range(len(lst)):
        if i + 1 == len(lst):
            result.append(lst[i])
        else:
            max_value = max(lst[i + 1:])
            result.append(max_value)
            result.append(lst[i])
            lst = list(filter(lambda x: x!= max_value, lst))
    return result
