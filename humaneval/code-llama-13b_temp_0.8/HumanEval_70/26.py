
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
    return lst if not lst else [min(lst)] + strange_sort_list(list(set(lst) - set([min(lst)]))) + [max(lst)] + strange_sort_list(list(set(lst) - set([max(lst)])))
    
    
    
