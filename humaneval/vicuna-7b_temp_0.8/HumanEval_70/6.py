
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
    min_val = min(lst)
    max_val = max(lst)
    for i in range(len(lst)):
        if lst[i] == min_val:
            result.append(max_val)
            result.append(min_val)
            result.append(lst[i])
        else:
            result.append(lst[i])
    return result