
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
        return []
    if len(lst) == 1:
        return lst
    
    min_lst = []
    max_lst = []
    
    for i in range(len(lst)):
        if lst[i] == min(lst):
            min_lst.append(lst[i])
        else:
            max_lst.append(lst[i])
        
    if len(min_lst) > 1:
        return min_lst + strange_sort_list(max_lst)
    else:
        return [min_lst[0]] + strange_sort_list(max_lst)
    
