
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
        return lst
    lst = lst[:]
    lst.sort()
    ordered_lst = [lst[0]]
    current_val = lst[0]
    for val in lst[1:]:
        if val == current_val:
            ordered_lst.append(val)
        else:
            #lst.remove(val)
            remove_val = min(lst[1:])
            ordered_lst.append(remove_val)
            lst.remove(remove_val)
            ordered_lst.append(val)
            current_val = val
    return ordered_lst
