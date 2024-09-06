
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
    srt_lst = []
    if len(lst) > 0:
        min_int = min(lst)
        srt_lst.append(min_int)
        lst.remove(min_int)
        max_int = max(lst)
        srt_lst.append(max_int)
        lst.remove(max_int)
    print(lst)
    for i in lst:
        srt_lst.append(i)
    return srt_lst

