
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

    min_n = min(lst)
    max_n = max(lst)
    
    lst = sorted(lst)
    new_lst = lst[0:max_n]
    new_lst = sorted(new_lst, reverse=True)
    
    new_lst.append(max_n)
    new_lst.append(min_n)
    
    return new_lst

