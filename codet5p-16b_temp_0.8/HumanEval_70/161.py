
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
    minimum = min(lst)
    minimum_index = lst.index(minimum)
    result.append(minimum)
    remaining = [x for x in lst if x!= minimum]
    maximum = max(remaining)
    maximum_index = remaining.index(maximum)
    result.extend([minimum, maximum])
    result.extend([minimum, maximum])
    remaining = [x for x in lst if x!= minimum and x!= maximum]
    minimum = min(remaining)
    minimum_index = remaining.index(minimum)
    result.append(minimum)
    result.append(maximum)
    result.append(minimum)
    result.append(maximum)
    return result
    
