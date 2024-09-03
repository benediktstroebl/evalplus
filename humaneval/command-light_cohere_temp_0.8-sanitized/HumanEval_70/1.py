def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, it means starting with the minimum value and going
    to the maximum of the remaining integers.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    return lst[::-1]