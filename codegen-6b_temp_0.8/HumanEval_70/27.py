
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
    min_val = min(lst)
    lst_copy = lst[:]
    lst_copy.remove(min_val)
    max_val = max(lst_copy)
    lst.remove(min_val)
    lst.remove(max_val)
    new_lst = [min_val, max_val] + lst
    return new_lst

lst = [1, 2, 3, 4]