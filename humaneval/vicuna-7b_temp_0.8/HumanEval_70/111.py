
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
    i = j = 0
    for k in range(n):
        while j < n and k < j:
            if lst[j] > lst[k]:
                j += 1
            else:
                i += 1
        if j < n and k < j:
            lst[i] = lst[j]
            j += 1
        else:
            lst[i] = lst[k]
            i += 1
    return lst
