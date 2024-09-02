
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
    lst_len = len(lst)
    if lst_len == 0:
        return []
    
    min = 0
    max = 0
    min_pos = -1
    max_pos = -1
    sorted_list = []
    sorted_count = 0
    
    while sorted_count < lst_len:
        if min == -1:
            min = min(lst)
            min_pos = lst.index(min)
            lst.pop(min_pos)
        elif max == -1:
            max = max(lst)
            max_pos = lst.index(max)
            lst.pop(max_pos)

        if min != -1 and max != -1:
            sorted_list.append(min)
            sorted_list.append(max)
            min = -1
            max = -1
            min_pos = -1
            max_pos = -1
            sorted_count += 2
    
    if lst:
        sorted_list.extend(lst)
    
    return sorted_list



