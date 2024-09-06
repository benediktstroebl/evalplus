
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
        return []
    small, big = lst[0], lst[0]
    for i in lst:
        if i < small:
            small = i
        elif i > big:
            big = i
    min_lst, max_lst = [], []
    for i in lst:
        if i == small:
            small = max(lst)
            min_lst.append(small)
        elif i == big:
            max_lst.append(i)
    return min_lst + max_lst + min_lst

