
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

    lst = sorted(lst)
    i = len(lst) - 1
    j = 1
    while i > 0:
        lst[i], lst[j] = lst[j], lst[i]
        i -= 2
        j += 2

    return lst

