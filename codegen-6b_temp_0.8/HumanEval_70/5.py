
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
    if not lst:
        return []
    
    lst = [-i for i in lst]
    # always starts with max
    sorted_lst = [max(lst)]
    while lst:
        # get max value
        sorted_lst.append(max(lst))
        # remove from list
        lst.remove(sorted_lst[-1])
        # always starts with min
        sorted_lst.append(min(lst))
        # remove from list
        lst.remove(sorted_lst[-1])
    
    return sorted_lst[:-1]
