
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
    def strange_sort(lst):
        if not lst:
            return []
        min_value = min(lst)
        max_value = max(lst)
        return [min_value] + strange_sort(
            [x for x in lst if x!= min_value and x!= max_value]
        ) + [max_value]
    return strange_sort(lst)
