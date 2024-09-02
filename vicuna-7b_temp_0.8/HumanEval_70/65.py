
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
    return sorted(lst, key=lambda x: x if x > 0 else min(lst[1:], key=lambda y: y if y > 0 else min(lst[2:], key=lambda z: z if z > 0 else min(lst[3:], key=lambda t: t))))
