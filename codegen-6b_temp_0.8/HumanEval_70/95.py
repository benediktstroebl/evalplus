
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
    n = len(lst)
    new_lst = [0] * n
    for i in range(n):
        min_val = min(lst)
        new_lst[i] = min_val
        lst.remove(min_val)
    for i in range(n-1, 0, -1):
        max_val = max(lst)
        new_lst[i] = max_val
        lst.remove(max_val)
    return new_lst

