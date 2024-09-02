
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
    sorted_lst = sorted(lst)
    min_val = sorted_lst[0]
    strange_lst = [min_val]
    for val in sorted_lst[1:]:
        min_val = min(min_val, val)
        strange_lst.append(max(val, min_val))
    return strange_lst

