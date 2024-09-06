
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
        return lst
    
    current_max = lst[0]
    current_min = lst[0]
    
    result = []
    for i in range(len(lst)):
        for item in lst:
            if item < current_min:
                current_min = item
            elif item > current_max:
                current_max = item
            else:
                pass
                
        result.append(current_min)
        lst.remove(current_min)
        current_min = lst[0]
        current_max = lst[0]
    
    return result
