
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
    # [1, 4, 2, 3]
    # [2, 4, 3]
    # [4, 3]
    # [4, 3]
    # [4, 3]
    # [4, 3]

    if len(lst) == 0:
        return lst
    else:
        return [min(lst)] + strange_sort_list(filter(lambda x: x != min(lst), lst)) + strange_sort_list(filter(lambda x: x != max(lst), lst)) + [max(lst)]
