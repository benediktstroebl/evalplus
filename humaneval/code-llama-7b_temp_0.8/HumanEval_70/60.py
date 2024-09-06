
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
    if len(lst) < 1:
        return lst
    new_lst = []
    count = 0
    while count < len(lst):
        min_lst = min(lst)
        lst.remove(min_lst)
        max_lst = max(lst)
        lst.remove(max_lst)
        new_lst.append(min_lst)
        new_lst.append(max_lst)
        count += 2
    return new_lst
