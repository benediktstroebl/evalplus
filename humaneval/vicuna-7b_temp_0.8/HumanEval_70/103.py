
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
    while i < len(lst) - 1:
        if lst[i] < lst[i + 1]:
            j = i
        else:
            j = i + 1
        lst[j], lst[i] = lst[i], lst[j]
        i = j + 1
    return lst
