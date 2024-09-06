
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
    length = len(lst)
    result = []
    for i in range(length // 2 + length % 2):
        result.append(min(lst))
        lst.pop(lst.index(min(lst)))
        if not lst:
            return result
        result.append(max(lst))
        lst.pop(lst.index(max(lst)))
    return result

