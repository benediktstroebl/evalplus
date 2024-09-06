
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
    min_num, max_num = (float("inf"), -float("inf"))
    for num in lst:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
    out_list = []
    while min_num < float("inf"):
        out_list.append(min_num)
        lst.remove(min_num)
        min_num = min(lst)
        max_num = max(lst)
    return out_list
        
