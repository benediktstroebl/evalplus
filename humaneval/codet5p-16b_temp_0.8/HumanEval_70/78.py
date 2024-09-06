
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

    if len(lst) <= 1:
        return lst
    if len(lst) == 2:
        return [min(lst), max(lst)]
    
    n = 1
    while n < len(lst):
        n *= 2
    
    n -= 1
    
    new_list = []
    for i in range(n+1):
        new_list.append(min(lst))
        lst.remove(min(lst))
    for i in range(n+1):
        new_list.append(max(lst))
        lst.remove(max(lst))
    
    return strange_sort_list(new_list)
    
    
