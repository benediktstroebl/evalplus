
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
        return []
    
    new_lst = []
    while lst:
        min_num = lst[0]
        for num in lst:
            if num < min_num:
                min_num = num
        lst.remove(min_num)
        new_lst.append(min_num)
        if lst:
            max_num = lst[0]
            for num in lst:
                if num > max_num:
                    max_num = num
            lst.remove(max_num)
            new_lst.append(max_num)
    
    return new_lst

