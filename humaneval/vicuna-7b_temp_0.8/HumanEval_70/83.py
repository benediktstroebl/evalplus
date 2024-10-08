
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
    n = len(lst)
    result = [lst[0]]
    for i in range(1, n):
        min_value = min(lst[i], lst[i-1])
        max_value = max(lst[i], lst[i-1])
        result.append((max_value, min_value))
        result.append(lst[i])
    return result
