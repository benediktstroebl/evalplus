
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
    sort_lst = []

    while len(lst) > 0:
        min_num = min(lst)
        sort_lst.append(min_num)
        lst.remove(min_num)
        max_num = max(lst)
        sort_lst.append(max_num)
        lst.remove(max_num)
        min_num = min(lst)
        sort_lst.append(min_num)
        lst.remove(min_num)

    return sort_lst
