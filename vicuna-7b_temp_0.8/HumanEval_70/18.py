
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
    lst = sorted(lst)
    result = []
    for i in range(len(lst)):
        result.append(lst[i])
        if (i+1) % 3 == 1 or (i+1) % 3 == 2:
            result.append(lst[i+1])
    return result
