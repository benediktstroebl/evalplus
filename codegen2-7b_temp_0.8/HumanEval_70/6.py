
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
    lst = [x for x in lst]
    lst.sort(reverse=True)
    if lst == []:
        return []
    min_val = min(lst)
    i = lst.index(min_val)
    nxt_val = lst[i+1]
    lst[i+1] = lst[i]
    lst[i] = nxt_val
    return lst
