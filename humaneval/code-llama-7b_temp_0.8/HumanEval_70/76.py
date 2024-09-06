
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
    #your code here
    lst_len = len(lst)
    if lst_len == 0:
        return []
    else:
        min_num = min(lst)
        lst.remove(min_num)
        max_num = max(lst)
        lst.remove(max_num)
        return [min_num, max_num] + strange_sort_list(lst)

