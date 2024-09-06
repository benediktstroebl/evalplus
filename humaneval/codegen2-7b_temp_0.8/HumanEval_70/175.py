
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
    if len(lst) < 2:
        return lst
    else:
        mid_idx = int((len(lst))/2)
        sorted_lst = strange_sort_list(lst[:mid_idx])
        sorted_lst += strange_sort_list(lst[mid_idx:])
        sorted_lst += strange_sort_list(sorted_lst)
        return sorted_l
