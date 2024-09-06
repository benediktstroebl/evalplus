
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

    i = 0
    j = 0
    l = []
    while i < len(lst):
        while j < len(lst):
            if lst[i] < lst[j]:
                l.append(lst[i])
                i += 1
                break
            elif lst[j] < lst[i]:
                l.append(lst[j])
                j += 1
                break
        if i < len(lst):
            l.append(lst[i])
            i += 1
        if j < len(lst):
            l.append(lst[j])
            j += 1
    return l

