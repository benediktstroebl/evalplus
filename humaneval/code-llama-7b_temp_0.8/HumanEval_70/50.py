
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
    if len(lst) < 2:
        return lst
    odd = lst[::2]
    even = lst[1::2]
    if len(lst) % 2 == 1:
        return [min(odd), max(even)] + odd + [max(odd)] + even + [min(even)]
    else:
        return [min(odd), max(even)] + odd + [min(even)] + even + [max(even)]

