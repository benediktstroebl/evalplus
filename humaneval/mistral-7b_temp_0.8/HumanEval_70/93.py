
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
    sorted_lst = []
    while len(lst) > 0:
        min_index = lst.index(min(lst))
        sorted_lst.append(lst[min_index])
        lst.remove(lst[min_index])
        max_index = lst.index(max(lst))
        sorted_lst.append(lst[max_index])
        lst.remove(lst[max_index])
    return sorted_lst

