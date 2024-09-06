
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
    while i < len(lst):
        if lst[i] < lst[j]:
            j += 1
            continue
        i += 1
        if j == len(lst):
            return lst[i:len(lst)]
        if lst[i] > lst[j]:
            i += 1
            continue
        j += 1
    return lst[:]
