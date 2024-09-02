
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
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > result[-1]:
            result.append(lst[i])
            continue
        idx_min = len(result) - 1
        for idx, value in enumerate(lst[i+1:]):
            if value < result[idx_min]:
                idx_min = idx + i + 1
        result.insert(idx_min, lst[i])
    return result
