
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
    if lst == []:
        return lst
    else:
        minimum = lst[0]
        maximum = lst[0]
        for i in lst[1:]:
            if i > maximum:
                maximum = i
            if i < minimum:
                minimum = i
        return (
            strange_sort_list(lst[:lst.index(maximum)+1]) +
            [minimum] +
            strange_sort_list(lst[lst.index(minimum)+1:])
