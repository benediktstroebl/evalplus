
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

    min_val = lst[0]
    max_val = lst[0]
    new_lst = []
    for n in lst:
        if n < min_val:
            min_val = n
        elif n > max_val:
            max_val = n
    for n in lst:
        if n < min_val:
            new_lst.append(n)
    new_lst.append(max_val)
    for n in lst:
        if n > max_val:
            new_lst.append(n)
    new_lst.append(min_val)
    return new_lst
