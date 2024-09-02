
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
    
    new_lst = []
    min_idx = 0
    max_idx = 0
    while min_idx < len(lst):
        min_val = lst[min_idx]
        max_val = 0
        for i in range(min_idx + 1, len(lst)):
            if lst[i] > max_val:
                max_val = lst[i]
                max_idx = i
        new_lst.append(min_val)
        new_lst.append(max_val)
        min_idx = max_idx + 1
        
    return new_lst
