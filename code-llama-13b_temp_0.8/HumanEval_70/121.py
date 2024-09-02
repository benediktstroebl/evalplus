
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

    # Task: sorting integer list
    # solution: iterative approach
    # first: minimum, then maximum, then minimum, then maximum, etc.
    # each time: 
    # - get the min/max, and place it to the end of the list
    # - remove it from original list
    # - repeat until original list is empty
    
    # base case
    if len(lst) == 0:
        return lst
    
    # the result list
    result = []
    
    # while there are any elements in the list
    while len(lst) > 0:
        # get the minimum element, and add it to the result list
        min_value = min(lst)
        result.append(min_value)
        
        # get the maximum element, and add it to the result list
        max_value = max(lst)
        result.append(max_value)
        
        # remove the min and max elements from original list
        lst.remove(min_value)
        lst.remove(max_value)

    # return the result
    return result
        
        
