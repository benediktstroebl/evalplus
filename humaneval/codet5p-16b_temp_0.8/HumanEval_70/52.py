
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

    
    result = []
    
    while lst:
        min_val = min(lst)
        lst = [x for x in lst if x!= min_val]
        max_val = max(lst)
        result.append(min_val)
        result.append(max_val)
        lst = [x for x in lst if x!= max_val]
    
    return result
    
    
