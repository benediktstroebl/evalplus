
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

    
    if len(lst) < 2:
        return lst
    
    min_value = min(lst)
    max_value = max(lst)
    strange_list = []
    
    for _ in range(len(lst)):
        if lst[0] < max_value:
            strange_list.append(max_value)
            lst.pop(0)
        else:
            lst.pop(0)
        if lst:
            if lst[0] < min_value:
                strange_list.append(min_value)
                lst.pop(0)
            else:
                lst.pop(0)
        
    strange_list.extend(lst)
    return strange_list

