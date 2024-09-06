
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
    mid = len(lst) // 2
    min_val = lst[mid]
    max_val = max(lst[mid+1:])
    result = [min_val]
    for i in range(mid, -1, -1):
        result.append(lst[i])
    return result + [max_val] + [result[-1]]
