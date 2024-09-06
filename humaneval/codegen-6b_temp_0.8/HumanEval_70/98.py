
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
    if lst:
        min_value = min(lst)
        max_value = max(lst)
        step = 0
        while lst:
            value = min_value + step
            if value in lst:
                lst.remove(value)
            elif value + 1 in lst:
                lst.remove(value + 1)
            step += 1
        return lst
    else:
        return []

import unittest

