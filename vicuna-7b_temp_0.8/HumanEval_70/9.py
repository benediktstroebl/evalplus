
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
    n = len(lst)
    if n == 1:
        return lst[0]
    result = []
    i = j = 0
    while i < n:
        while j < n and lst[j] <= lst[i]:
            j += 1
        result.append(lst[i])
        i += 1
        j = i
    result.append(lst[j])
    return result
