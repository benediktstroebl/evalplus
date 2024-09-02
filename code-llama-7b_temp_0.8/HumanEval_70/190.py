
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
    list_sort = sorted(lst)
    length = len(list_sort)
    i = 0
    while i < length - 1:
        list_sort.append(list_sort[0])
        list_sort.remove(list_sort[0])
        list_sort.remove(list_sort[-1])
        i += 1
    return list_sort
