
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
        return lst
    min_num = min(lst)
    sort_lst = lst.copy()
    sort_lst.sort()
    sort_lst = [num for num in sort_lst if num!= min_num]
    sort_lst.insert(0, min_num)
    return strange_sort_list(sort_l
