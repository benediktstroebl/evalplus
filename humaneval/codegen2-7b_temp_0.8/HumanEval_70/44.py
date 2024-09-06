
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
    lst_rev = lst[::-1]
    sort_list = []
    for i in lst:
        sort_list.extend([i]*(len(lst)-i))
    for i in range(len(lst)):
        lst[i] = lst_rev[i]
    return l
