
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
    if len(lst) == 0:
        return lst
    
    minimum = min(lst)
    maximum = max(lst)
    
    if minimum == maximum:
        return lst
    
    result = [minimum, maximum]
    
    remaining = []
    
    for number in lst:
        if number != minimum and number != maximum:
            remaining.append(number)
            
    if len(remaining) == 0:
        return result
    
    next_minimum = min(remaining)
    
    for number in remaining:
        if number != next_minimum:
            result.append(number)
            
    next_remaining = []
    
    for number in remaining:
        if number != next_minimum:
            next_remaining.append(number)
            
    result.append(next_minimum)
    
    return result + strange_sort_list(next_remaining)
