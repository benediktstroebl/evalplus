
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
    
    sort_list = [min(lst[:i + 1]) for i in range(len(lst))]
    
    if len(lst) % 2 == 1:
        sort_list.append(max(lst[len(lst)//2:]))
    else:
        sort_list.append(max(lst[len(lst)//2:]))
        sort_list.append(min(lst[:len(lst)//2]))
    
    return sort_list
