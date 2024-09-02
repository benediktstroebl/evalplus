
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
    for i in lst:
        if i == 0:
            result.append(i)
            continue
        min_value = min(lst)
        max_value = max(lst)
        for j in range(1, len(lst)):
            if lst[j] <= min_value:
                min_value = lst[j]
            if lst[j] >= max_value:
                max_value = lst[j]
        result.append(min_value)
        result.append(max_value)
        result.append(lst[0])
        result.append(lst[1])
        result.append(lst[2])
    return result
