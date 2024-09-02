
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

    if len(lst) <= 1:
        return lst
    small = min(lst)
    small_index = lst.index(small)
    del lst[small_index]
    big = max(lst)
    big_index = lst.index(big)
    del lst[big_index]

    return [small] + strange_sort_list(lst) + [big]

