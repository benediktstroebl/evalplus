
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
    minimum = min(lst)
    maximum = max(lst)
    result = [minimum]
    while len(lst) > 0:
        for item in lst:
            if item != minimum and item != maximum:
                result.append(item)
        lst = [minimum, maximum]
        minimum = min(lst)
        maximum = max(lst)
        result.append(minimum)
        lst.remove(minimum)
    return result

