
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
    new_lst = []
    while lst:
        min = min(lst)
        max = max(lst)
        new_lst.append(min)
        new_lst.append(max)
        lst.remove(min)
        lst.remove(max)
    return new_lst
