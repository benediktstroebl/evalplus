
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
    result = []
    for i in range(n):
        l = [lst[i]]
        for j in range(1, n):
            if j == n - 1:
                l.append(min(lst[j:j+1]))
            elif lst[j] > lst[j+1]:
                l.append(lst[j])
            else:
                l.append(lst[j+1])
        result.append(l)
    return result
