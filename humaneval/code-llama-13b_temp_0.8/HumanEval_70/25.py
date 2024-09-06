
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
    remaining = lst[:]
    while len(remaining):
        result.append(min(remaining))
        remaining.remove(min(remaining))
        if len(remaining):
            result.append(max(remaining))
            remaining.remove(max(remaining))
    return result

