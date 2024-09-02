
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
    if lst == []:
        return []
    min_val = min(lst)
    max_val = max(lst)
    sort_lst = []
    for val in lst:
        sort_lst.append(min_val)
        if val == max_val:
            sort_lst.append(val)
        else:
            sort_lst.append(max_val)
    return sort_lst

