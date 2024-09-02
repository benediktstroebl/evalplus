
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
    new_lst = []
    for num in lst:
        max_num = max(lst)
        min_num = min(lst)
        if num > max_num:
            new_lst.append(num)
            lst.remove(num)
            lst.append(max_num)
        elif num < min_num:
            new_lst.append(num)
            lst.remove(num)
            lst.append(min_num)
    return strange_sort_list(
