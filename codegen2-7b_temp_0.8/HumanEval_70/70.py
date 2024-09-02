
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
    lst = lst[:]
    while lst:
        item = lst.pop(0)
        for index in range(len(lst)):
            if lst[index] > item:
                lst[index - 1], lst[index] = lst[index], lst[index - 1]
    return lst
